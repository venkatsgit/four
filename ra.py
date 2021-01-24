import random
from fourd.pipelines import FourdPipeline

if __name__ == "__main__":
    pipeline = FourdPipeline()
    l_numbers = [11, 7, 17, 27,19, 23, 12,13, 9,18]
    #l_numbers = [11, 7]
    existing_numbers = pipeline.get_numbers(6000,7000)
    for i in range(100):
        rand_number = random.randint(6000,7000)
        if(not (str(rand_number) in existing_numbers) ):
            total_value_of_digits = 0;
            for c in str(rand_number):
                total_value_of_digits += int(c)
            if(total_value_of_digits in l_numbers):
                print(f" the random number {rand_number} and the total value of all digits {total_value_of_digits}");
