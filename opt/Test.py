from def_main import main


if __name__ == "__main__":
    main()

print("HelloWorld")

# numpyライブラリをインポート
import numpy as np

# 整数型の配列を用意
arr_int32 = np.array([100, 200, 300, 400, 500], dtype=np.int32)
print(arr_int32)

# 浮動小数点型の配列を用意
arr_float = np.array([0.1, 0.2, 0.3, 0.4, 0.5], dtype=np.float64)
print(arr_float)

# 配列通しの計算を + で表現できます。
arr_sum = arr_int32 + arr_float
print(arr_sum)