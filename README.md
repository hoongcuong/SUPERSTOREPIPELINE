# Sales Data ETL Pipeline
Pipeline Data Engineering phân tích dữ liệu bán hàng từ CSV và API tỷ giá,sau đó lưu trữ và trực quan hóa dữ liệu.

## Mục tiêu
- Thu thập dữ liệu bán hàng từ CSV và tỷ giá từ ExchangeRate-API.
- Xử lý và lưu trữ vào PostgreSQL.
- Tạo báo cáo doanh thu (VND) và biểu đồ chuyên nghiệp.

## Công cụ
- **Python**: `pandas`, `requests`, `sqlalchemy`, `matplotlib`, `seaborn`
- **PostgreSQL**: Lưu trữ dữ liệu
- **Docker**: Đóng gói và triển khai
- **ExchangeRate-API** (key mẫu: `2de11a29b893a9c53ede5688`)

## Pipeline
1. **Extract**: Đọc dữ liệu từ `sales_data.csv` và gọi API tỷ giá USD → VND.
2. **Transform**: Làm sạch dữ liệu, tính toán `Total Sales` theo VND.
3. **Load**: Lưu dữ liệu vào PostgreSQL (`sales_table`).
4. **Analyze**: Tạo báo cáo, biểu đồ doanh thu theo sản phẩm, khu vực và thời gian.

## Hướng dẫn chạy
1. Cài đặt: `pip install -r requirements.txt`.
2. Cấu hình PostgreSQL (user/password) trong `etl_pipeline.py`.
3. Đặt file `sales_data.csv` vào thư mục.
4. Chạy: `python etl_pipeline.py`.

## Kết quả
- Bảng `sales_table` trong PostgreSQL.
- Biểu đồ: `sales_by_product.png`, `sales_by_region.png`, `sales_by_date.png`.

  👤 Thông tin tác giả
👨‍💻 GitHub: @hoongcuong
🌐 LinkedIn: https://www.linkedin.com/in/nghongcuong/
📧 Email: hongcuong0626@gmail.com
