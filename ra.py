import random
from fourd.pipelines import FourdPipeline

if __name__ == "__main__":
    pipeline = FourdPipeline()
    existing_numbers = pipeline.get_numbers(1000,2000)
    for i in range(10):
        rand_number = random.randint(1000,2000)
        if(not (str(rand_number) in existing_numbers) ):
            print(rand_number)