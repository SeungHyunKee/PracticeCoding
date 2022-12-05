import numpy as np

# 6. 난수의 재연 : 실행 마다 결과 동일
# 랜덤한 값이 실행할때 마다 변경되지 않도록 'Seed' 만든다
# 딥러닝 하고나서 학습결과가(다른pc에서도) 동일하게 나오게 하기위해 사용(단, 일반적인, kuda 에도 seed 걸어줘야됨)
np.random.seed(7777)  # seed 번호는 아무거나 주면 됨
print(np.random.randint(0, 10, (2, 3)))