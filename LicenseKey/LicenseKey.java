//Zhenqiao He	zxh151630
public class LicenseKey {

	public static void main(String[] args) {
		String input=args[0];
		int k=Integer.parseInt(args[1]);
		String res="";
		int num=0;
		while(input.charAt(0)=='-')	input=input.substring(0);
		input=input.toUpperCase();
		for(int i=input.length()-1;i>=0;i--){
			char c=input.charAt(i);
			if(c=='-')	continue;
			res=c+res;
			num++;
			if(num==k&&i!=0){
				res='-'+res;
				num=0;
			}
		}
		System.out.println(res);

	}

}
