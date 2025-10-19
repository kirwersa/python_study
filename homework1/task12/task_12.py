from mat2 import Mat2


def main():
    print("orig matix")
    m_0 = Mat2([1, 2], [3, 4])
    print(m_0)
    m_1 = Mat2([1, 2], [3, 4])
    m_s = m_0 + m_1
    print("sum matix")
    print(m_s)
    m_m = m_0 * 2
    print("mutl matix")
    print(m_m)


if __name__ == "__main__":
    main()
