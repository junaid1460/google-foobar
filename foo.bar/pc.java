import java.util.Random;

class pc{
    public static void main(String argc[]){
        int x[] = new int[2000];
        for(int i =0;i<2000;i++){
            x[i] = i + 2 *2 + i * 2* 4 * (new Random()).nextInt();
        }
        System.out.println(answer(x));
    }
    public static int answer(int []l){
        int i,j,k,count = 0;
        if(l.length < 3 || l.length >2000)
            return 0;
        else{
            
            for(i = 0;i<l.length-2;++i){
                if(l[i] == 1 && l[i + 1] == 1){
                    count += l.length - (i + 2);
                    continue;
                }
                for(j = i +1;j<l.length -1;++j){
                    if(l[j]%l[i] == 0)
                        for(k = j +1;k < l.length;k++){
                            if(l[k]%l[j] == 0)
                                count += 1;
                        }
                }
            }
        }
        return count;
    }
}