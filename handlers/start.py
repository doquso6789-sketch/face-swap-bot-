import cv2
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

swapper = get_model(
    "inswapper_128.onnx",
    download=True,
    download_zip=True
)

def swap_faces(source_path, target_path, output_path):

    source_img = cv2.imread(source_path)
    target_img = cv2.imread(target_path)

    source_faces = app.get(source_img)

    if not source_faces:
        raise Exception("Không tìm thấy khuôn mặt trong ảnh nguồn")

    source_face = source_faces[0]

    target_faces = app.get(target_img)

    if not target_faces:
        raise Exception("Không tìm thấy khuôn mặt trong ảnh đích")

    result = target_img.copy()

    for face in target_faces:
        result = swapper.get(
            result,
            face,
            source_face,
            paste_back=True
        )

    cv2.imwrite(output_path, result)

    return output_path
