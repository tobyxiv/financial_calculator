"""
Due: Saturday, December 14, 2019 at 11:59pm

@author: Patrick Mahan, Dylan Wirawan, Gabriel Singer, Aidan Mcerlean
"""

# Home Page
homeHTML = """
<style>body{background-color: #ffb366;}</style>
<p><br /><center><h1>Financial Calculator</h1></p>
<p><center><h3>Created By: Patrick Mahan, Dylan Wirawan, Gabriel Singer, Aidan Mcerlean</h3></p>
<p><center><img src="https://i.postimg.cc/65xHD96K/imageedit-2-6626502388.png" style="width:300px;height:400px;"></p>
<p><button type="button" class="block" style="display: block; width: 100%; border: none; background-color: #4CAF50; padding: 14px 28px; font-size: 16px; cursor: pointer; text-align: center;"><a href="calc_home">Enter</button></a></p>
""".strip()

# Calculators Page
calc_splashHTML = """
<style>body{background-color: #ffb366;}</style>
<p>&nbsp;</p>
<p><center><h3>Choose what you would like to calculate below:</p>
<p>&nbsp;</p>
<center><button type="button" style="background-color: #4CAF50; border: none; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;"><a href="/pv_bond">Present Value of a Bond</button></a>
<p>&nbsp;</p>
<center><button type="button" style="background-color: ##008CBA; border: none; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;"><a href="/perp">Perpetuity</button></a>
<p>&nbsp;</p>
<center><button type="button" style="background-color: #f44336; border: none; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px;"><a href="/mort">Monthly Mortgage Payments</button></a>
""".strip()

# Present Value of a Bond
pv_bondHTML = """
<style>body{background-color: #ffb366;}</style>
<p><br /><center><h1>Present Value of a Bond</h1></p>
<p>&nbsp;</p>
<p><center>Enter your parameters below, then click submit:</p>
<form action="/pv_bond_result">

<p>
Interest Rate %:<br /> 
<input name="irate" type="number" step="0.01" value="1" /> 
<br /> 

Compounding Frequency:
<br /> 
<input name="comp_fq" type="number" step="0.01" value="2" /> 

<br />
Coupon Pmt:
<br /> 
<input name="p_cf" type="number" step="0.01" value="10" /> 

<br /> 
Face (Future) Value:
<br /> 
<input name="f_v" type="number" step="0.01" value="1000" /> 

<br /> 
Number of Years:
<br /> 
<input name="n_y" type="number" step="0.01" value="1" /> 

<br /><br /> 
<input type="submit" value="Submit" />
</p>

<p>&nbsp;</p>
<a href='/calc_home'>Choose a different calculator</a>

</form>
""".strip()

# Present Value of a Bond - Result Page
pv_bond_resultHTML = """
<p>&nbsp;</p>
<p><center>You entered:</p>
<table>

<thead>

<tr nth-child(even)>
<th padding: 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #4CAF50; color: white;><center>Parameters</th>
<th padding: 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #4CAF50; color: white;><center>Value</th>
</tr>
</thead>


<tbody>

<tr>
<td><center>Interest Rate %</td>
<td><center>{irate_field}</td>
</tr>

<tr>
<td><center>Compounding Frequency</td>
<td><center>{comp_fq_field}</td>
</tr>

<tr>
<td><center>Coupon Pmt</td>
<td><center>{p_cf_field}</td>
</tr>

<tr>
<td><center>Face (Future) Value</td>
<td><center>{f_v_field}</td>
</tr>

<tr>
<td><center>Number of Years</td>
<td><center>{n_y_field}</td>
</tr>

</tbody>
</table>

<p><h1><center>Present Value of your bond is <span style="background-color: #FFFF00">{pv_field}</span></h1></p>

<p>&nbsp;</p>
<p><img src="https://i.postimg.cc/FHX9kKM7/home-icon.png" vertical-align="top" style="width:30px;height:30px;">&nbsp;&nbsp;&nbsp;<a href='/'>Go to home page</a></p>
<p>&nbsp;</p>
<img src="https://i.postimg.cc/65xHD96K/imageedit-2-6626502388.png" vertical-align="top" style="width:30px;height:40px;">&nbsp;&nbsp;&nbsp;<a href='/calc_home'>Do another calculation</a>
""".strip()

# Perpetuity
perpHTML = """
<style>body{background-color: #ffb366;}</style>
<p><br /><center><h1>Perpetuity</h1></p>
<p>&nbsp;</p>
<p><center>Enter your parameters below, then click submit:</p>
<form action="/perp_result">

<p>
Interest Rate %:<br /> 
<input name="irate" type="number" step="0.01" value="1" /> 
<br /> 

<br />
Coupon Pmt:
<br /> 
<input name="p_cf" type="number" step="0.01" value="10" /> 

<br /><br /> 
<input type="submit" value="Submit" />
</p>

<p>&nbsp;</p>
<a href='/calc_home'>Choose a different calculator</a>

</form>
""".strip()

# Perpetuity - Result Page
perp_resultHTML = """
<p>&nbsp;</p>
<p><center>You entered:</p>
<table>
<tbody>

<th padding: 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #4CAF50; color: white;><center>Parameters</th>
<th padding: 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #4CAF50; color: white;><center>Value</th>

<tr>
<td><center>Interest Rate %</td>
<td><center>{irate_field}</td>
</tr>

<tr>
<td><center>Coupon Pmt</td>
<td><center>{p_cf_field}</td>
</tr>

</tbody>
</table>

<p><h1><center>The value of your perpetuity is <span style="background-color: #FFFF00">{pv_field}</span></h1></p>

<p>&nbsp;</p>
<p><img src="https://i.postimg.cc/FHX9kKM7/home-icon.png" vertical-align="top" style="width:30px;height:30px;">&nbsp;&nbsp;&nbsp;<a href='/'>Go to home page</a></p>
<p>&nbsp;</p>
<img src="https://i.postimg.cc/65xHD96K/imageedit-2-6626502388.png" vertical-align="top" style="width:30px;height:40px;">&nbsp;&nbsp;&nbsp;<a href='/calc_home'>Do another calculation</a>
""".strip()

# Monthly Mortgage Payments
mortHTML = """
<style>body{background-color: #ffb366;}</style>
<p><br /><center><h1>Monthly Mortgage Payments</h1></p>
<p>&nbsp;</p>
<p><center>Enter your parameters below, then click submit:</p>
<form action="/mort_result">

<p>
Loan Amt:
<br /> 
<input name="loan" type="number" step="0.01" value="1000" /> 
<br/>

Yearly Interest %:<br /> 
<input name="irate" type="number" step="0.01" value="1" /> 
<br />

Years:<br /> 
<input name="loan_term" type="number" step="0.01" value="30" /> 
<br />


<br /><br /> 
<input type="submit" value="Submit" />
</p>

<p>&nbsp;</p>
<a href='/calc_home'>Choose a different calculator</a>

</form>
""".strip()

# Monthly Mortgage Payments - Results Page
mort_resultHTML = """
<p>&nbsp;</p>
<p><center>The user entered:</p>
<table>
<tbody>

<tr>
<td><center>Loan Amt</td>
<td><center>{loan_field}</td>
</tr>

<tr>
<td><center>Yearly Interest %</td>
<td><center>{irate_field}</td>
</tr>

<tr>
<td><center>Years</td>
<td><center>{loan_term_field}</td>
</tr>

</tbody>
</table>

<p><h1><center>Your monthly payment amount is <span style="background-color: #FFFF00">{mo_pmt_field}</span></h1></p>

<p>&nbsp;</p>
<p><img src="https://i.postimg.cc/FHX9kKM7/home-icon.png" vertical-align="top" style="width:30px;height:30px;">&nbsp;&nbsp;&nbsp;<a href='/'>Go to home page</a></p>
<p>&nbsp;</p>
<img src="https://i.postimg.cc/65xHD96K/imageedit-2-6626502388.png" vertical-align="top" style="width:30px;height:40px;">&nbsp;&nbsp;&nbsp;<a href='/calc_home'>Do another calculation</a>
""".strip()

# Error Page
errorMessageHTML = """
<p>&nbsp;</p>
<p><center>{error_field}</p>
<p>&nbsp;</p>
<p><center><img src="https://i.postimg.cc/25Frpqms/broken-calc.jpg" style="width:200x;height:200px;"></p>
<p>&nbsp;</p>
<a href='/calc_home'><center>Try Again</a>
""".strip()