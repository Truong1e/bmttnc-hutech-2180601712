from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("***************************MENU****************************")
    print("** 1. Thêm Sinh Viên.                                    **")
    print("** 2. Cập nhật thông tin sinh viên bởi ID.               **")
    print("** 3. Xóa Sinh Viên Bởi ID.                              **")
    print("** 4. Tìm Kiếm Sinh Viên Theo Tên.                       **")
    print("** 5. Sắp Xếp Sinh Viên Theo Điểm Trung Bình.            **")
    print("** 6. Sắp Xếp Sinh Viên Theo Tên Chuyên Ngành.           **")
    print("** 7. Hiển Thị Danh Sách Sinh Viên.                      **")
    print("** 0. Thoát.                                             **")
    print("***********************************************************")
    
    key = int(input("Nhập Tùy Chọn: "))
    if (key == 1):
        print("\n1. Thêm Sinh Viên.")
        qlsv.nhapSinhVien()
        print("\nThêm Sinh Viên Thành Công!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập Nhật Thông Tin Sinh Viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa Sinh Viên.")
            print("Nhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh Viên Có ID = ", ID, "Đã Bị Xóa.")
            else:
                print("\nSinh Viên Có ID = ", ID, "Không Tồn Tại.")
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm Kiếm Sinh Viên Theo Tên.")
            print("\nNhập Tên Để Tìm Kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp Xếp Sinh Viên Theo Điểm Trung Bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp Xếp Sinh Viên Theo Tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển Thị Danh Sách Sinh Viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Sinh Viên Trống!")
    elif (key == 0):
        print("\nBạn Đã chọn thoát Chương Trình")
        break
    else:
        print("\nKhông có chức năng này")
        print("\nHãy Chọn Chức Năng trong hộp menu")