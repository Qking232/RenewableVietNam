# GridTwinVN

Bản trực quan hoá mô hình lưới điện Việt Nam `Grid_Model_Vietnam.xiidm`, dựng theo cùng cách đã làm
với lưới truyền tải Pháp trong GridTwin.

## Nguồn gốc

Mô hình được tái dựng từ **Sơ đồ kết dây cơ bản Hệ thống điện Việt Nam 2025** do NSMO phát hành,
bản dự thảo ngày 30/9/2024, khổ A0 phủ toàn quốc từ 500 kV xuống từng ngăn lộ 110 kV.

Đây là **réseau de référence tĩnh**, không phải Point Figé. Toàn bộ công suất phát và phụ tải bằng 0.
Không có trạng thái máy cắt thực tế, không có kết quả tính trào lưu công suất. Muốn có ảnh chụp vận
hành phải có SCADA cộng bộ ước lượng trạng thái.

## Chạy

```bash
cd GridTwinVN && python -m http.server 8777
```

Rồi mở http://localhost:8777. Phải mở qua máy chủ web, không mở trực tiếp bằng `file://` vì trang cần
đọc các file JSON và SVG.

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `index.html`, `assets/app.js`, `assets/app.css` | Ứng dụng một trang, không phụ thuộc mạng ngoài trừ ảnh nền bản đồ |
| `assets/vendor/` | Leaflet đóng gói sẵn |
| `data/grid.json` | Payload chính: trạm, đường dây, thống kê |
| `data/inventory.json` | Bảng kiểm kê |
| `data/suspect_lines.json` | Danh sách tuyến nghi ghép sai đầu nối |
| `data/geojson/` | Bản sao GeoJSON để mở bằng QGIS |
| `sld/`, `nad/` | Thư viện sơ đồ dựng sẵn bằng PowSyBl, kèm `sld/manifest.json` |
| `build/` | Các script sinh dữ liệu |

## Dựng lại dữ liệu

```bash
python build/export_data.py
python build/render_diagrams.py
```

`export_data.py` đọc thẳng file XIIDM bằng PowSyBl và sinh toàn bộ dữ liệu cho giao diện.
`render_diagrams.py` dựng sẵn sơ đồ một sợi cho mọi cấp điện áp của các trạm 500 kV và 220 kV,
cộng các nhà máy trên 100 MW và 60 trạm 110 kV có sơ đồ chi tiết nhất.

## Quy ước hiển thị

Màu đường dây theo đúng quy ước của chính bản vẽ NSMO:

| Màu | Cấp điện áp |
|---|---|
| Xanh lá | 500 kV |
| Đỏ | 220 kV |
| Xanh dương | 110 kV |

Nét đứt là công trình dự kiến vào vận hành năm 2025. Chấm đặc là trạm biến áp, vòng rỗng là sân phân
phối nhà máy, hình vuông là trạm cắt.

## Kiểm soát chất lượng

Giao diện có một tab riêng ghi rõ lớp dữ liệu nào đọc trực tiếp từ bản vẽ, lớp nào là ước lượng, lớp
nào còn thiếu. Bộ dò tự động đánh dấu các tuyến có chiều dài đường chim bay vượt xa mức hợp lý của cấp
điện áp, vốn gần như luôn là lỗi trùng tên địa danh khi khâu biên. Các tuyến này bị ẩn mặc định trên
bản đồ và được liệt kê đầy đủ trong tab Chất lượng dữ liệu.
