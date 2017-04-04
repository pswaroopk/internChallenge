//Zhenqiao he 	zxh151630
public class StringToInteger {

	public static void main(String[] args) {
		String input=args[0];
		int index = 0, sign = 1, res = 0;
	    //check whether it is empty string
	    if(input.length() == 0)	System.out.println(0);
	    //to remove spaces
	    while(input.charAt(index) == ' ' && index < input.length())
	        index ++;
	    //to handle signs
	    if(input.charAt(index) == '+' || input.charAt(index) == '-'){
	        sign = input.charAt(index) == '+' ? 1 : -1;
	        index ++;
	    }  
	    //to convert number and avoid overflow
	    while(index < input.length()){
	        int digit = input.charAt(index) - '0';
	        if(digit < 0 || digit > 9) break;
	        //to check if res will be overflow after 10 times and add digit
	        if(Integer.MAX_VALUE/10 < res || Integer.MAX_VALUE/10 == res && Integer.MAX_VALUE %10 < digit){
	            if(sign == 1)	System.out.println(Integer.MAX_VALUE);
	            else	System.out.println(Integer.MIN_VALUE);
	    	}
	        res = 10 * res + digit;
	        index ++;
	    }
	    res=res * sign;
	    System.out.println(res);
	}

}
