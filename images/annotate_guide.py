# annotate_guide.py ----------------------------------------------------------
# Regenerates every user-guide illustration image from the base screenshots.
# Run from this images/ folder:  python annotate_guide.py
# Number badges have a white ring so they stand out from the red box borders.
#   mode="inside"  -> badge inside the top-right corner (default; adjacent boxes)
#   mode="outside" -> badge just outside the corner (well-separated boxes)

from PIL import Image, ImageDraw, ImageFont
red = (200, 30, 45); white = (255, 255, 255)

def font(sz):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", sz)
    except Exception:
        return ImageFont.load_default()

def annotate(src, dst, boxes, mode="inside"):
    im = Image.open(src).convert("RGB"); W, H = im.size
    d = ImageDraw.Draw(im)
    r = max(24, int(0.0085 * W)); lw = max(4, int(0.0016 * W)); pad = lw + 2
    hw = max(4, int(0.0020 * W))
    f = font(int(1.3 * r))
    for fx0, fy0, fx1, fy1, lab in boxes:
        x0, y0, x1, y1 = int(fx0*W), int(fy0*H), int(fx1*W), int(fy1*H)
        for w in range(lw):
            d.rectangle([x0-w, y0-w, x1+w, y1+w], outline=red)
        if mode == "outside":
            bx = min(W - r - hw - 1, x1 + r // 2)
            by = max(r + hw + 1, y0 - r // 2)
        else:
            bx = x1 - r - pad - hw
            by = y0 + r + pad + hw
        d.ellipse([bx-r-hw, by-r-hw, bx+r+hw, by+r+hw], fill=white)
        d.ellipse([bx-r, by-r, bx+r, by+r], fill=red)
        tb = d.textbbox((0, 0), lab, font=f)
        d.text((bx-(tb[2]-tb[0])/2-tb[0], by-(tb[3]-tb[1])/2-tb[1]), lab, fill="white", font=f)
    im.save(dst)

annotate("guide_caseboard.png", "guide_caseboard_annotated.png", [
    (0.006, 0.123, 0.275, 0.971, "1"),
    (0.280, 0.130, 0.993, 0.283, "2"),
    (0.280, 0.293, 0.993, 0.968, "3")])

Image.open("guide_caseboard.png").convert("RGB").crop((0, 230, 1075, 1865)).save("guide_settings_zoom.png")

annotate("guide_settings_zoom.png", "guide_settings_annotated.png", [
    (0.028, 0.035, 0.972, 0.069, "1"),
    (0.028, 0.170, 0.972, 0.243, "2"),
    (0.028, 0.347, 0.972, 0.423, "3"),
    (0.028, 0.521, 0.972, 0.576, "4"),
    (0.028, 0.586, 0.972, 0.641, "5"),
    (0.028, 0.680, 0.972, 0.753, "6"),
    (0.028, 0.855, 0.972, 0.913, "7")], mode="outside")

annotate("guide_behaviour.png", "guide_behaviour_annotated.png", [
    (0.004, 0.205, 0.252, 0.60, "1"),
    (0.256, 0.205, 0.986, 0.345, "2"),
    (0.256, 0.35, 0.686, 0.82, "3"),
    (0.69, 0.35, 0.986, 0.82, "4")])

annotate("guide_connections.png", "guide_connections_annotated.png", [
    (0.004, 0.125, 0.252, 0.45, "1"),
    (0.256, 0.122, 0.985, 0.185, "2"),
    (0.256, 0.19, 0.748, 0.525, "3"),
    (0.752, 0.19, 0.99, 0.525, "4"),
    (0.256, 0.54, 0.99, 0.86, "5")])

annotate("guide_evidence_bypass.png", "guide_evidence_bypass_annotated.png", [
    (0.004, 0.135, 0.252, 0.72, "1"),
    (0.256, 0.18, 0.985, 0.24, "2"),
    (0.256, 0.245, 0.985, 0.565, "3"),
    (0.256, 0.585, 0.985, 0.965, "4")])

annotate("guide_evidence_messages.png", "guide_evidence_messages_annotated.png", [
    (0.004, 0.15, 0.252, 0.205, "1"),
    (0.256, 0.095, 0.985, 0.39, "2"),
    (0.256, 0.41, 0.985, 0.965, "3")])

annotate("guide_intake.png", "guide_intake_annotated.png", [
    (0.004, 0.135, 0.31, 0.285, "1"),
    (0.004, 0.295, 0.31, 0.625, "2"),
    (0.004, 0.635, 0.31, 0.87, "3"),
    (0.004, 0.878, 0.31, 0.93, "4"),
    (0.33, 0.155, 0.99, 0.81, "5")])

print("Regenerated annotated guide images.")
