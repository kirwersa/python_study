from warehousebin import WarehouseBin


def main():
    container = WarehouseBin()
    container.add(10)
    container.add(20)
    container.add(10)
    # print(container.__len__())
    print(len(container))
    # print(container.__contains__(10))
    print(10 in container)
    for x in container:
        print(x)


if __name__ == '__main__':
    main()
