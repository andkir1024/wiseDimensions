 (Ctrl+Shift+P) Python: Create Environment
инициализхация виртуального окружения
python -m venv .venv

установка необходимых зависимостей
pip install -r Requirements.txt

сохранение необходимых зависимостей
pip freeze > Requirements.txt

git config --global user.email "andkir@mail.ru"
git config --global user.name "andkir1024"

sudo apt-get install libzbar0
sudo apt-get install tesseract-ocr-rus -y

python -c "import open3d as o3d; \
           mesh = o3d.geometry.TriangleMesh.create_sphere(); \
           mesh.compute_vertex_normals(); \
           o3d.visualization.draw(mesh, raw_mode=True)"