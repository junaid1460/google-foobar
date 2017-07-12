import java.math.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;



class Util{
  protected static BigInteger BigIntegerZERO = BigInteger.ZERO;
  protected static BigInteger BigIntegerONE = BigInteger.ONE;
  protected static BigInteger BigIntegerTWO = BigInteger.valueOf(2);
  protected static BigInteger BigIntegerTHREE=BigInteger.valueOf(3);
  protected static BigInteger FactorialBreakpoint = BigInteger.valueOf(96);
  protected static BigDecimal BigDecimalZERO = BigDecimal.ZERO;
  protected static BigDecimal BigDecimalONE = BigDecimal.ONE;
  protected static BigDecimal BigDecimalTWO = new BigDecimal(2);
  protected static BigDecimal BigDecimalFOUR = new BigDecimal(4);
  
  public static BigInteger sqrt(BigInteger number)
  {
    return sqrt(number, BigIntegerONE);
  }

  public static BigDecimal sqrt(BigDecimal number, RoundingMode rounding)
  {
    return sqrt(number, BigDecimalONE, rounding);
  }

  protected static BigInteger sqrt(BigInteger number, BigInteger guess)
  {
    // ((n/g) + g)/2: until same result twice in a row
//    BigInteger result = number.divide(guess).add(guess).divide(BigIntegerTWO);
//    if(result.compareTo(guess) == 0)
//      return result;
//
//    return sqrt(number, result);

    // redoing this to avoid StackOverFlow
    BigInteger result = BigIntegerZERO;
    BigInteger flipA = result;
    BigInteger flipB = result;
    boolean first = true;
    while( result.compareTo(guess) != 0 )
    {
      if(!first)
        guess = result;
      else
        first=false;

      result = number.divide(guess).add(guess).divide(BigIntegerTWO);
      // handle flip flops
      if(result.equals(flipB))
        return flipA;

      flipB = flipA;
      flipA = result;
    }
    return result;

  }
  public static BigDecimal sqrt(BigDecimal number, BigDecimal guess, RoundingMode rounding)
  {
    BigDecimal result = BigDecimalZERO;
    BigDecimal flipA = result;
    BigDecimal flipB = result;
    boolean first = true;
    while( result.compareTo(guess) != 0 )
    {
      if(!first)
        guess = result;
      else
        first=false;

      result = number.divide(guess, rounding).add(guess).divide(BigDecimalTWO, rounding);
      // handle flip flops
      if(result.equals(flipB))
        return flipA;

      flipB = flipA;
      flipA = result;
    }
    return result;
  }
}


class Answer {   
    public static void main(String args[]){
        answer("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111");
    }
     static public BigDecimal log(BigDecimal x)
        {
                /* the value is undefined if x is negative.
                */
                if ( x.compareTo(BigDecimal.ZERO) < 0 )
                        throw new ArithmeticException("Cannot take log of negative "+ x.toString() ) ;
                else if ( x.compareTo(BigDecimal.ONE) == 0 )
                {
                        /* log 1. = 0. */
                        return scalePrec(BigDecimal.ZERO, x.precision()-1) ;
                }
                else if ( Math.abs(x.doubleValue()-1.0) <= 0.3 )
                {
                        /* The standard Taylor series around x=1, z=0, z=x-1. Abramowitz-Stegun 4.124.
                        * The absolute error is err(z)/(1+z) = err(x)/x.
                        */
                        BigDecimal z = scalePrec(x.subtract(BigDecimal.ONE),2) ;
                        BigDecimal zpown = z ;
                        double eps = 0.5*x.ulp().doubleValue()/Math.abs(x.doubleValue()) ;
                        BigDecimal resul = z ;
                        for(int k= 2;; k++)
                        {
                                zpown = multiplyRound(zpown,z) ;
                                BigDecimal c = divideRound(zpown,k) ;
                                if ( k % 2 == 0)
                                        resul = resul.subtract(c) ;
                                else
                                        resul = resul.add(c) ;
                                if ( Math.abs(c.doubleValue()) < eps)
                                        break;
                        }
                        MathContext mc = new MathContext( err2prec(resul.doubleValue(),eps) ) ;
                        return resul.round(mc) ;
                }
                else
                {
                        final double xDbl = x.doubleValue() ;
                        final double xUlpDbl = x.ulp().doubleValue() ;

                        /* Map log(x) = log root[r](x)^r = r*log( root[r](x)) with the aim
                        * to move roor[r](x) near to 1.2 (that is, below the 0.3 appearing above), where log(1.2) is roughly 0.2.
                        */
                        int r = (int) (Math.log(xDbl)/0.2) ;

                        /* Since the actual requirement is a function of the value 0.3 appearing above,
                        * we avoid the hypothetical case of endless recurrence by ensuring that r >= 2.
                        */
                        r = Math.max(2,r) ;

                        /* Compute r-th root with 2 additional digits of precision
                        */
                        BigDecimal xhighpr = scalePrec(x,2) ;
                        BigDecimal resul = root(r,xhighpr) ;
                        resul = log(resul).multiply(new BigDecimal(r)) ;

                        /* error propagation: log(x+errx) = log(x)+errx/x, so the absolute error
                        * in the result equals the relative error in the input, xUlpDbl/xDbl .
                        */
                        MathContext mc = new MathContext( err2prec(resul.doubleValue(),xUlpDbl/xDbl) ) ;
                        return resul.round(mc) ;
                }
        }
         static public BigDecimal pow(final BigDecimal x, final BigDecimal y)
        {
                if( x.compareTo(BigDecimal.ZERO) < 0 )
                        throw new ArithmeticException("Cannot power negative "+ x.toString()) ;
                else if( x.compareTo(BigDecimal.ZERO) == 0 )
                        return BigDecimal.ZERO ;
                else
                {
                        /* return x^y = exp(y*log(x)) ;
                        */
                        BigDecimal logx = log(x) ;
                        BigDecimal ylogx = y.multiply(logx) ;
                        BigDecimal resul = exp(ylogx) ;

                        /* The estimation of the relative error in the result is |log(x)*err(y)|+|y*err(x)/x| 
                        */
                        double errR = Math.abs(logx.doubleValue()*y.ulp().doubleValue()/2.)
                                + Math.abs(y.doubleValue()*x.ulp().doubleValue()/2./x.doubleValue()) ;
                        MathContext mcR = new MathContext( err2prec(1.0,errR) ) ;
                        return resul.round(mcR) ;
                }
        }
    public static int answer(String n) { 
        BigDecimal value = new BigDecimal(n);
        BigDecimal sq = Util.sqrt(value, RoundingMode.HALF_EVEN);
        BigDecimal v = new BigDecimal(1);
        value.
        v= pow(new BigDecimal(2),sq);
        pr(v);


        // Your code goes here.
        return 0;
    } 



    public static void pr(Object e){
        System.out.println(e);
    }
}