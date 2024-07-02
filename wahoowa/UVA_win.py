def celebrate():
    """Celebrate UVA's win"""
    loop_iter = int(input("Enter a number: "))
    if loop_iter <= 10:
        print("Thats too low of a number")
        loop_iter = 100
    for _ in range(loop_iter):
        print('Wahoowa!!')