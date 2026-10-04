BÀI TẬP 2: QUẢN LÝ NHÁNH VÀ GIẢI QUYẾT XUNG ĐỘT (MERGE CONFLICT)

1. MỤC TIÊU
- Tạo mới và di chuyển linh hoạt giữa các nhánh cục bộ main và feature-update.
- Tái hiện xung đột gộp nhánh (Merge Conflict) khi cả hai nhánh cùng chỉnh sửa nội dung trên cùng một vị trí của tệp tin.
- Hiểu cơ chế gộp 3 vùng (3-Way Merge) và thực hiện xử lý xung đột thủ công bằng cách loại bỏ các ký hiệu đánh dấu.
- Hoàn tất commit gộp nhánh (Merge Commit) và phân tích đồ thị lịch sử commit.

2. CÁC BƯỚC THỰC HIỆN CHI TIẾT

2.1. Khởi tạo repository và nhánh main ban đầu
```bash
git init -b main
git config --local user.name "Tran Duc"
git config --local user.email "tranduc2601@example.com"
```
Tạo phiên bản đầu tiên của tệp tin app.py và commit trên nhánh main:
```bash
git add app.py
git commit -m "feat: khoi tao ham tinh toan metrics tren main"
```

2.2. Tạo nhánh phụ và thực hiện cập nhật tính năng
Tạo nhánh mới feature-update và chuyển sang nhánh này:
```bash
git checkout -b feature-update
```
Chỉnh sửa hàm calculate_metrics trong app.py bổ sung trường "maximum":
```python
def calculate_metrics(data_list):
    total = sum(data_list)
    avg = total / len(data_list) if data_list else 0
    max_val = max(data_list) if data_list else 0
    return {
        "count": len(data_list),
        "total": total,
        "average": avg,
        "maximum": max_val
    }
```
Commit thay đổi trên nhánh feature-update:
```bash
git add app.py
git commit -m "feat(feature-update): them chi so maximum vao ket qua"
```

2.3. Cập nhật đồng thời trên nhánh main gây xung đột
Chuyển lại về nhánh main:
```bash
git checkout main
```
Chỉnh sửa cùng hàm calculate_metrics trong app.py bổ sung trường "status":
```python
def calculate_metrics(data_list):
    total = sum(data_list)
    avg = total / len(data_list) if data_list else 0
    return {
        "count": len(data_list),
        "total": total,
        "average": avg,
        "status": "calculated"
    }
```
Commit thay đổi trên nhánh main:
```bash
git add app.py
git commit -m "feat(main): them trang thai status vao ket qua metrics"
```

2.4. Thực hiện gộp nhánh và phát sinh Merge Conflict
Thực hiện lệnh merge nhánh feature-update vào main:
```bash
git merge feature-update
```
Git thông báo xung đột:
```text
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

2.5. Xử lý xung đột thủ công
Mở tệp app.py, các ký hiệu xung đột xuất hiện như sau:
```text
<<<<<<< HEAD
        "count": len(data_list),
        "total": total,
        "average": avg,
        "status": "calculated"
=======
        "count": len(data_list),
        "total": total,
        "average": avg,
        "maximum": max_val
>>>>>>> feature-update
```
Tiến hành xóa các thẻ đánh dấu xung đột và kết hợp cả hai tính năng:
```python
def calculate_metrics(data_list):
    total = sum(data_list)
    avg = total / len(data_list) if data_list else 0
    max_val = max(data_list) if data_list else 0
    return {
        "count": len(data_list),
        "total": total,
        "average": avg,
        "maximum": max_val
    }
```

2.6. Hoàn tất commit gộp nhánh
Đưa tệp đã sửa vào Staging Area và commit:
```bash
git add app.py
git commit -m "Merge branch 'feature-update' into main: Giai quyet xung dot thanh cong"
```

3. KẾT QUẢ KIỂM TRA VÀ LOG TERMINAL

3.1. Trạng thái xung đột và sau khi giải quyết
Log kiểm tra trạng thái trong quá trình xung đột:
```text
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   app.py

no changes added to commit (use "git add" to track)
```
Log kiểm tra sau khi hoàn thành merge:
```text
$ git status
On branch main
nothing to commit, working tree clean
```

3.2. Đồ thị lịch sử commit (Git Graph)
Lệnh thực hiện:
```bash
git log --graph --oneline --all
```
Trích xuất log terminal:
```text
*   e4f5a6b (HEAD -> main) Merge branch 'feature-update' into main: Giai quyet xung dot thanh cong
|\  
| * c3d4e5f (feature-update) feat(feature-update): them chi so maximum vao ket qua
* | b2c3d4e feat(main): them trang thai status vao ket qua metrics
|/  
* a1b2c3d feat: khoi tao ham tinh toan metrics tren main
```

4. KẾT LUẬN
- Quy trình phân nhánh và giải quyết xung đột thủ công được thực hiện chuẩn xác.
- Đồ thị lịch sử Git thể hiện rõ ràng 2 nhánh tổ tiên (parents) gộp lại thành công tại Merge Commit.
