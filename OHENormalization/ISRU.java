	public static double ISRU(double n)
	{
		int z = 1;
		if(n==0 || n==1)
			return n;
		else
			return n/Math.sqrt(z+n*n);
	}
