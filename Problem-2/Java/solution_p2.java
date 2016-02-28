public class solution_p2 {
    
    public static int fibSum(int number) {
        int twoNumsAgo = 1;
        int oneNumAgo = 2;
        int sum = 0;
        int fib = 3;
        while (fib < number) {
            fib = oneNumAgo + twoNumsAgo;
            if (fib > number) {
                break;
            }
            if (fib % 2 == 0) {
                sum += fib;
            }
            twoNumsAgo = oneNumAgo;
            oneNumAgo = fib;
        }
        if (sum > 0) {
            sum += 2;
        }
        return sum;
        
    }

    public static void main(String[] args) {
        assert fibSum(10) == 10 : "The sum of the even fibonacci numbers less than 10 should be equal to 10";
        assert fibSum(100) == 44 : "The sum of the even fibonacci numbers less than 100 should be equal to 44";
        System.out.println(fibSum(4000000)); // = 4613732
    }
}
