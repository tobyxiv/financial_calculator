"""
Due: Saturday, December 14, 2019 at 11:59pm

@author: Patrick Mahan, Dylan Wirawan, Gabriel Singer, Aidan Mcerlean
"""

from flask import Flask,request

from html_calc import calc_splashHTML, pv_bondHTML, pv_bond_resultHTML
from html_calc import perpHTML, perp_resultHTML
from html_calc import mortHTML, mort_resultHTML
from html_calc import errorMessageHTML

from html_calc import homeHTML

import numpy as np


app = Flask(__name__)

# Home Page
@app.route('/')
def homepage():
    return homeHTML

# Calculators Page
@app.route('/calc_home')
def calculator_landing_page():
    return calc_splashHTML

# Present Value of a Bond
@app.route('/pv_bond')
def pv_bond():
    return pv_bondHTML

# Present Value of a Bond - Result Page
@app.route('/pv_bond_result')
def pv_bond_result():
    try: 
        irate = float(request.args.get('irate'))/100
        comp_fq = float(request.args.get('comp_fq'))
        p_cf = float(request.args.get('p_cf'))
        f_v = float(request.args.get('f_v'))
        n_y = float(request.args.get('n_y'))
        pv_name = np.pv(irate/comp_fq, comp_fq*n_y, p_cf, f_v, when='end')
        return pv_bond_resultHTML.format(irate_field=irate,comp_fq_field=comp_fq, p_cf_field=p_cf, f_v_field=f_v, n_y_field = n_y, pv_field = pv_name)

    except ZeroDivisionError:
        return errorMessageHTML.format(error_field = 'You may not have an interest rate of zero.')
    except ValueError:
        return errorMessageHTML.format(error_field = 'Please enter integers.')
    except:
        return errorMessageHTML.format(error_field = 'Something went wrong. Try entering the most logical integer values.')

# Perpetuity
@app.route('/perp')
def perp():
    return perpHTML

# Perpetuity - Result Page
@app.route('/perp_result')
def perp_result():
    try:
        irate = float(request.args.get('irate'))/100
        p_cf = float(request.args.get('p_cf'))
        pv_name = p_cf/irate
        return perp_resultHTML.format(irate_field=irate, p_cf_field=p_cf, pv_field=pv_name)

    except ZeroDivisionError:
        return errorMessageHTML.format(error_field = 'You may not have an interest rate of zero.')
    except ValueError:
        return errorMessageHTML.format(error_field = 'Please enter integers.')
    except:
        return errorMessageHTML.format(error_field = 'Something went wrong. Try entering the most logical integer values.')

# Monthly Mortgage Payments
@app.route('/mort')
def mort():
    return mortHTML

# Monthly Mortgage Payments - Results Page
@app.route('/mort_result')
def mort_result():
    try: 
        loan = float(request.args.get('loan'))
        irate = float(request.args.get('irate'))/100
        loan_term = float(request.args.get('loan_term'))
        
        a_irate = irate/12
        a_loan_term = loan_term*12
        num = a_irate*((1+a_irate)**(a_loan_term))
        denom = ((1+a_irate)**(a_loan_term))-1
        
        mo_pmt = loan*num/denom
        
        return mort_resultHTML.format(loan_field=loan, irate_field=irate, loan_term_field=loan_term, mo_pmt_field = mo_pmt)

    except ZeroDivisionError:
        return errorMessageHTML.format(error_field = 'You may not have an interest rate of zero.')
    except ValueError:
        return errorMessageHTML.format(error_field = 'Please enter integers.')
    except:
        return errorMessageHTML.format(error_field = 'Something went wrong. Try entering the most logical integer values.')

# Error Page
@app.route('/error')
def error():
    return errorMessageHTML

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)