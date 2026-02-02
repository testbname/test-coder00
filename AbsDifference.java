public class AbsDifference {
    
    /**
     * 计算两个整数的绝对值之差
     * @param a 第一个整数
     * @param b 第二个整数
     * @return |a| - |b| 的结果
     */
    public static int absDifference(int a, int b) {
        return Math.abs(a) - Math.abs(b);
    }
    
    // 测试方法
    public static void main(String[] args) {
        // 测试用例
        System.out.println("absDifference(5, 3) = " + absDifference(5, 3));       // 2
        System.out.println("absDifference(-5, 3) = " + absDifference(-5, 3));     // 2
        System.out.println("absDifference(5, -3) = " + absDifference(5, -3));     // 2
        System.out.println("absDifference(-5, -3) = " + absDifference(-5, -3));   // 2
        System.out.println("absDifference(0, 0) = " + absDifference(0, 0));       // 0
        System.out.println("absDifference(-10, 5) = " + absDifference(-10, 5));   // 5
    }
}