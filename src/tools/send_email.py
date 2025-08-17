import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from typing import Optional
from livekit.agents import function_tool, RunContext

@function_tool()    
async def send_email(
    context: RunContext,  # type: ignore
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Send an email through Gmail.
    Args:
        to_email: Recipient email address
        subject: Email subject line
        message: Email body content
    """
    # ...existing code...
