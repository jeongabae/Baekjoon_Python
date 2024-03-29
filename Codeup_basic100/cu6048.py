a, b = map(int, input().split())
print(a<b) #print("True" if a<b else "False")이랑 같은 역할.
"""
참고
어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

비교/관계연산자 < (less than sign) 는
왼쪽의 값이 오른쪽 값 보다 작은 경우 True(참)로 계산하고,
그 외의 경우에는 False(거짓)로 계산한다.

비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
그 결과를 True(참), 또는 False(거짓)로 계산해 주는 연산자이다.

비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.

True(참) 또는 False(거짓) 값으로만 표현하고 저장하는 값을 불(bool)/불리언(boolean) 값이라고 한다.
정수, 실수, 문자, 문자열과 마찬가지로 또 다른 형태의 데이터형(data type)이다.
"""