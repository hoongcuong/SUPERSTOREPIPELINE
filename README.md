# Sales Data ETL Pipeline
Pipeline Data Engineering phân tích dữ liệu bán hàng từ CSV và API tỷ giá.

## Mục tiêu
- Thu thập dữ liệu bán hàng từ CSV và tỷ giá từ ExchangeRate-API.
- Xử lý và lưu trữ vào PostgreSQL.
- Tạo báo cáo doanh thu (VND) và biểu đồ chuyên nghiệp.

## Công cụ
- Python (Pandas, SQLAlchemy, Matplotlib, Seaborn).
- PostgreSQL.
- ExchangeRate-API (Key: 2de11a29b893a9c53ede5688).

## Pipeline
1. **Extract**: Đọc CSV và gọi API tỷ giá USD -> VND.
2. **Transform**: Làm sạch, tính doanh thu USD/VND.
3. **Load**: Lưu vào PostgreSQL.
4. **Analyze**: Báo cáo và trực quan hóa.

## Hướng dẫn chạy
1. Cài đặt: `pip install -r requirements.txt`.
2. Cấu hình PostgreSQL (user/password) trong `etl_pipeline.py`.
3. Đặt file `sales_data.csv` vào thư mục.
4. Chạy: `python etl_pipeline.py`.

## Kết quả
- Bảng `sales_table` trong PostgreSQL.
- Biểu đồ: `sales_by_product.png`, `sales_by_region.png`, `sales_by_date.png`.