from reportlab.pdfgen import canvas
import io
from fastapi.responses import StreamingResponse

async def generate_pdf(content: str):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, content)
    pdf.save()
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=document.pdf"})
