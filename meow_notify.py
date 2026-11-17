"""通过 MeoW API 将签到结果推送到手机。"""

from __future__ import annotations

import logging
import os
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)

DEFAULT_CATEGORY = "贴吧签到"


def get_push_url() -> str:
    """从环境变量读取 MeoW 接收地址。"""
    return os.environ.get("MEOW_PUSH_URL", "").strip()


def _valid_endpoint(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme == "https" and parsed.netloc == "api.chuckfang.com"


def send_message(
    title: str,
    message: str,
    *,
    push_url: str | None = None,
    category: str = DEFAULT_CATEGORY,
) -> bool:
    """通过 MeoW API 发送纯文本手机通知。"""
    endpoint = (push_url or get_push_url()).strip()
    if not endpoint:
        logger.info("未配置 MEOW_PUSH_URL，跳过 MeoW 手机推送")
        return False
    if not _valid_endpoint(endpoint):
        logger.error("MeoW 推送地址无效：仅允许 https://api.chuckfang.com/ 下的地址")
        return False

    payload = {
        "title": title.strip() or "贴吧签到结果",
        "msg": message,
        "category": category.strip(),
    }

    try:
        resp = requests.post(endpoint, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != 200 or data.get("data") is False:
            logger.error(
                "MeoW 推送失败: status=%s msg=%s",
                data.get("status"),
                str(data.get("msg", "未知错误"))[:200],
            )
            return False
        logger.info("MeoW 手机推送成功")
        return True
    except (requests.RequestException, ValueError) as exc:
        # 不记录完整异常文本，避免私人推送 URL 出现在 Actions 日志中。
        logger.error("MeoW 推送异常: %s", type(exc).__name__)
        return False
