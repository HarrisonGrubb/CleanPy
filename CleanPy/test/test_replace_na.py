import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append("../../")

import CleanPy as rp

# Helper codes
toy_data = pd.DataFrame({"x":[None, 4, 6], "y": [2, None, None], "z": [3.6, 8.5, None]})
toy_all_na = pd.DataFrame({"x":[None, None, None], "y": [None, None, None], "z": [None, None, None]})
toy_no_na = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
toy_string = pd.DataFrame({"x":["Yes", "No"], "y": [None, "Yes"], "z": ["No", "Yes"]})

# Test data type
print (toy_data)

def test_correct_input():
    """
    Test that the function returns an error if
    the input type is wrong
    """
    with pytest.raises(TypeError):
        rp.replace_na("Input Data", columns="x")

def test_column_type():
    """
    Test that incorrect column raises Type Error
    """
    with pytest.raises(TypeError):
        rp.replace_na(toy_string, columns="x")

def test_output_type():
    """
    Test that the output type is also a  dataframe
    """
    columns_1 = toy_data.columns.values
    columns_2 = toy_all_na.columns.values
    columns_3 = toy_no_na.columns.values
    assert type(rp.replace_na(toy_data, columns_1)) == pd.DataFrame
    assert type(rp.replace_na(toy_no_na, columns_3)) == pd.DataFrame

# Test for the functionality of the function

def test_functionality():
    """
    Test for the correct functionality of the function
    """
    toy_result = pd.DataFrame({"x":[5,4,6], "y":[2,2,2], "z":[3.6,8.5,6.05]})
    all_na_result = pd.DataFrame({"x":[0,0,0], "y":[0,0,0], "z":[0,0,0]})
    no_na_result = pd.DataFrame({"x":[1, 2, 3, 4], "y": [1, 2, 3, 4], "z": [1, 2, 3, 4]})
    columns_1 = toy_data.columns.values
    columns_2 = toy_all_na.columns.values
    columns_3 = toy_no_na.columns.values
    a = rp.replace_na(toy_data, columns_1) == toy_result
    c = rp.replace_na(toy_no_na, columns_3) == no_na_result
    assert a.all(axis = None)
    assert c.all(axis = None)
    with pytest.raises(KeyError):
        rp.replace_na(toy_string, ["x"])
           
def test_remove_nas_nona():
    """
    Test functionality of remove=True but dataframe has no nas
    """
    #return same dataframe
    pd.util.testing.assert_frame_equal(rp.replace_na(toy_no_na, columns=["y"], remove=True), toy_no_na) 
    
def test_replace_min():
    """
    Test functionality of replace=min
    """
    toy_result_min = pd.DataFrame({"x":[None, 4, 6], "y": [2, None, None], "z": [3.6, 8.5, 3.6]})
    pd.util.testing.assert_frame_equal(rp.replace_na(toy_data, columns=["z"], replace="min"), toy_result_min) 
    
def test_replace_max():
    """
    Test functionality of replace=max
    """
    toy_result_max = pd.DataFrame({"x":[None, 4, 6], "y": [2, None, None], "z": [3.6, 8.5, 8.5]})
    pd.util.testing.assert_frame_equal(rp.replace_na(toy_data, columns=["z"], replace="max"), toy_result_max)

def test_replace_median():
    """
    Test functionality of replace=median
    """
    toy_result_median = pd.DataFrame({"x":[None, 4, 6], "y": [2, None, None], "z": [3.6, 8.5, 6.05]})
    pd.util.testing.assert_frame_equal(rp.replace_na(toy_data, columns=["z"], replace="median"), toy_result_median)
    
# If the data frame contains all missing values(NAs)
columns_2 = toy_all_na.columns.values
def test_input_contains_all_missingvalues():
    """
    Raise Type Error if all values are missing
    """
    with pytest.raises(TypeError):
          rp.replace_na(toy_all_na, columns_2)
