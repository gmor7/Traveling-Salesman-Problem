import pytest
from cities import *

def test_compute_each_distance_1():
    """
    Testing whether the distance between only two locations (one and two) are
    identical, from location one to two and returning from location two to one.
    """
    road_map1 = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),\
                ('Delaware', 'Dover', '39.161921', '-75.526755')]
    
    assert compute_each_distance(road_map1) ==\
           [9.38, 9.38]
                      
def test_compute_each_distance_2():
    """
    Testing whether the distance between only two locations (one and two) are
    identical, from location one to two and returning from location two to one.
    """
    road_map2 = [('Delaware', 'Dover', '39.161921', '-75.526755'),\
                ('Minnesota', 'Saint Paul', '44.95', '-93.094')]
    
    assert compute_each_distance(road_map2) ==\
           [18.49, 18.49]

def test_compute_each_distance_3():
    """
    Testing whether the distance returning is 0 if only one location is given
    """
    road_map3 = [('Delaware', 'Dover', '39.161921', '-75.526755')]
    
    assert compute_each_distance(road_map3) ==\
    [0]

def test_compute_each_distance_4():
    """
    Testing whether function runs as expected with numerous locations.
    """
    road_map4 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    
    assert compute_each_distance(road_map4) ==\
    [44.09, 7.68, 3.5, 26.86, 47.19, 74.49, 3.31, 12.34, 
     3.86, 32.36, 16.53, 29.39, 19.78, 17.37, 16.12]

def test_compute_each_distance_5():
    """
    Testing whether function returns two zero values if given the same location
    twice (and only twice).
    """
    road_map5 = [('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
                 ('Indiana', 'Indianapolis', '39.790942', '-86.147685')]
    
    assert compute_each_distance(road_map5) ==\
    [0, 0]

def test_compute_total_distance_1():
    """
    Testing whether compute_total_distance working correctly for three cities
    """
    road_map1 = [('Kentucky', 'Frankfort', '38.197274', '-84.86311'),\
                ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                ('Minnesota', "Saint Paul", '44.95', '-93.094')]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance_2():
    """
    Testing whether compute_total_distance working correctly for three cities
    """
    road_map2 = [('Montana', 'Helana', '46.595805', '-112.027031'),\
                 ('New Mexico', 'Santa Fe', '35.667231', '-105.964575'),\
                 ('Oregon', 'Salem', '44.931109', '-123.029159')]
    
    assert compute_total_distance(road_map2)==\
           pytest.approx(12.49748+19.41699+11.12736, 0.01)   
   
def test_compute_total_distance_3():
    """
    Testing whether compute_total_distance returns 0 if same city given twice
    """
    road_map3 = [('Montana', 'Helana', '46.595805', '-112.027031'),\
                 ('Montana', 'Helana', '46.595805', '-112.027031')]
    
    assert compute_total_distance(road_map3)==\
           pytest.approx(0)
           
def test_compute_total_distance_4():
    """
    Testing whether compute_total_distance returns 0 if only one city is given
    """
    road_map4 = [('Montana', 'Helana', '46.595805', '-112.027031')]
    
    assert compute_total_distance(road_map4)==\
           pytest.approx(0)
           
def test_compute_total_distance_5():
    """
    Testing whether compute_total_distance returns correct figure when given
    entire original road_map
    """
    road_map5 = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),\
                 ('Alaska', 'Juneau', '58.301935', '-134.41974'),\
                 ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
                 ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
                 ('California', 'Sacramento', '38.555605', '-121.468926'),\
                 ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),\
                 ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
                 ('Georgia', 'Atlanta', '33.76', '-84.39'),\
                 ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
                 ('Idaho', 'Boise', '43.613739', '-116.237651'),\
                 ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
                 ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
                 ('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
                 ('Kansas', 'Topeka', '39.04', '-95.69'),\
                 ('Kentucky', 'Frankfort', '38.197274', '-84.86311'),\
                 ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),\
                 ('Maine', 'Augusta', '44.323535', '-69.765261'),\
                 ('Maryland', 'Annapolis', '38.972945', '-76.501157'),\
                 ('Massachusetts', 'Boston', '42.2352', '-71.0275'),\
                 ('Michigan', 'Lansing', '42.7335', '-84.5467'),\
                 ('Minnesota', 'Saint Paul', '44.95', '-93.094'),\
                 ('Mississippi', 'Jackson', '32.32', '-90.207'),\
                 ('Missouri', 'Jefferson City', '38.572954', '-92.189283'),\
                 ('Montana', 'Helana', '46.595805', '-112.027031'),\
                 ('Nebraska', 'Lincoln', '40.809868', '-96.675345'),\
                 ('Nevada', 'Carson City', '39.160949', '-119.753877'),\
                 ('New Hampshire', 'Concord', '43.220093', '-71.549127'),\
                 ('New Jersey', 'Trenton', '40.221741', '-74.756138'),\
                 ('New Mexico', 'Santa Fe', '35.667231', '-105.964575'),\
                 ('New York', 'Albany', '42.659829', '-73.781339'),\
                 ('North Carolina', 'Raleigh', '35.771', '-78.638'),\
                 ('North Dakota', 'Bismarck', '48.813343', '-100.779004'),\
                 ('Ohio', 'Columbus', '39.962245', '-83.000647'),\
                 ('Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'),\
                 ('Oregon', 'Salem', '44.931109', '-123.029159'),\
                 ('Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'),\
                 ('Rhode Island', 'Providence', '41.82355', '-71.422132'),\
                 ('South Carolina', 'Columbia', '34', '-81.035'),\
                 ('South Dakota', 'Pierre', '44.367966', '-100.336378'),\
                 ('Tennessee', 'Nashville', '36.165', '-86.784'),\
                 ('Texas', 'Austin', '30.266667', '-97.75'),\
                 ('Utah', 'Salt Lake City', '40.7547', '-111.892622'),\
                 ('Vermont', 'Montpelier', '44.26639', '-72.57194'),\
                 ('Virginia', 'Richmond', '37.54', '-77.46'),\
                 ('Washington', 'Olympia', '47.042418', '-122.893077'),\
                 ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444'),\
                 ('Wyoming', 'Cheyenne', '41.145548', '-104.802042')] 
    
    assert compute_total_distance(road_map5)==\
           pytest.approx(1060.09, 0.1)      

def test_swap_cities_1():
    """
    Testing whether swap_cities swaps index 1 with index 4 and computes the
    correct new total distance
    """
    road_map1 = [('Wyoming', 'Cheyenne', '41.145548', '-104.802042'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444'),\
                 ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                 ('Alabama', 'Montgomery', '32.361538', '-86.279118'),\
                 ('Virginia', 'Richmond', '37.54', '-77.46')]
    swapped_road_map1 =[('Wyoming', 'Cheyenne', '41.145548', '-104.802042'),\
                 ('Virginia', 'Richmond', '37.54', '-77.46'),\
                 ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                 ('Alabama', 'Montgomery', '32.361538', '-86.279118'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444')]
    total_distance2 = compute_total_distance(swapped_road_map1)
    
    assert swap_cities(road_map1, 1, 4) ==\
    (swapped_road_map1,total_distance2)

def test_swap_cities_2():
    """
    Testing whether swap_cities swaps index 8 with index 13 and computes the
    correct new total distance
    """
    road_map2 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    swapped_road_map2 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    total_distance3 = compute_total_distance(swapped_road_map2)
    
    assert swap_cities(road_map2, 8, 13) ==\
    (swapped_road_map2,total_distance3)

def test_swap_cities_3():
    """
    Testing whether swap_cities swaps index 0 with index 1 and computes the
    correct new total distance
    """
    road_map3 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    
    swapped_road_map3 = [('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    total_distance4 = compute_total_distance(swapped_road_map3)

    assert swap_cities(road_map3, 0, 1) ==\
    (swapped_road_map3,total_distance4)

def test_swap_cities_4(): # index1 = 0, index2 = 14
    """
    Testing whether swap_cities swaps the first and last indexes (index 0 and 
    index 14 in this test) and computes the correct new total distance
    """
    road_map4 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Alaska', 'Juneau', '58.301935', '-134.41974')]
    
    swapped_road_map4 = [('Alaska', 'Juneau', '58.301935', '-134.41974'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),\
    ('Illinois', 'Springfield', '39.78325', '-89.650373'),\
    ('Idaho', 'Boise', '43.613739', '-116.237651'),\
    ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
    ('Georgia', 'Atlanta', '33.76', '-84.39'),\
    ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
    ('Delaware', 'Dover', '39.161921', '-75.526755'),\
    ('Connecticut', 'Hartford', '41.767', '-72.677'),\
    ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
    ('California', 'Sacramento', '38.555605', '-121.468926'),\
    ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),\
    ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
    ('Washington', 'Olympia', '47.042418', '-122.893077'),\
    ('Iowa', 'Des Moines', '41.590939', '-93.620866')]
    total_distance5 = compute_total_distance(swapped_road_map4)

    assert swap_cities(road_map4, 0, 14) ==\
    (swapped_road_map4,total_distance5)

def test_swap_cities_5():
    """
    Testing whether swap_cities does nothing if given the same index
    """
    road_map5 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685')]
    
    swapped_road_map5 = [('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
    ('Indiana', 'Indianapolis', '39.790942', '-86.147685')]
    total_distance6 = compute_total_distance(swapped_road_map5)
    assert swap_cities(road_map5, 1, 1) ==\
            (swapped_road_map5,total_distance6)

def test_shift_cities():
    """
    Testing whether shift_cities is working with 5 cities"
    """
    road_map1 = [('Montgomery', 'Alabama', '32.36', '-86.28'),\
                 ('Juneau', 'Alaska', '58.3', '-134.42'),\
                 ('Phoenix', 'Arizona', '33.45', '-112.07'),\
                 ('Little Rock', 'Arkansas', '34.74', '-92.33'),\
                 ('Sacramento', 'California', '38.56', '-121.47')]
    
    shifted_1 = [('Sacramento', 'California', '38.56', '-121.47'),\
                 ('Montgomery', 'Alabama', '32.36', '-86.28'),\
                 ('Juneau', 'Alaska', '58.3', '-134.42'),\
                 ('Phoenix', 'Arizona', '33.45', '-112.07'),\
                 ('Little Rock', 'Arkansas', '34.74', '-92.33')]
    
    assert shift_cities(road_map1) ==\
    (shifted_1)

def test_shift_cities_2():
    """
    Testing whether shift_cities is working with 10 cities
    """
    road_map2 = [('South Dakota', 'Pierre', '44.367966', '-100.336378'),\
                 ('Tennessee', 'Nashville', '36.165', '-86.784'),\
                 ('Texas', 'Austin', '30.266667', '-97.75'),\
                 ('Utah', 'Salt Lake City', '40.7547', '-111.892622'),\
                 ('Vermont', 'Montpelier', '44.26639', '-72.57194'),\
                 ('Virginia', 'Richmond', '37.54', '-77.46'),\
                 ('Washington', 'Olympia', '47.042418', '-122.893077'),\
                 ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444'),\
                 ('Wyoming', 'Cheyenne', '41.145548', '-104.802042')]
    
    shifted_2 = [('Wyoming', 'Cheyenne', '41.145548', '-104.802042'),\
                 ('South Dakota', 'Pierre', '44.367966', '-100.336378'),\
                 ('Tennessee', 'Nashville', '36.165', '-86.784'),\
                 ('Texas', 'Austin', '30.266667', '-97.75'),\
                 ('Utah', 'Salt Lake City', '40.7547', '-111.892622'),\
                 ('Vermont', 'Montpelier', '44.26639', '-72.57194'),\
                 ('Virginia', 'Richmond', '37.54', '-77.46'),\
                 ('Washington', 'Olympia', '47.042418', '-122.893077'),\
                 ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444')]
    
    assert shift_cities(road_map2) ==\
    (shifted_2)

def test_shift_cities_3():
    """
    Testing that shift_cities is working with only two cities
    """
    road_map3 = [('Washington', 'Olympia', '47.042418', '-122.893077'),\
                 ('Wisconsin', 'Madison', '43.074722', '-89.384444')]
    
    shifted_3 = [('Wisconsin', 'Madison', '43.074722', '-89.384444'),\
                 ('Washington', 'Olympia', '47.042418', '-122.893077')]
    
    assert shift_cities(road_map3) ==\
    (shifted_3)
    
def test_shift_cities_4():
    """
    Testing shift_cities with a different road_map
    """
    road_map4 = [('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
                 ('Georgia', 'Atlanta', '33.76', '-84.39'),\
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
                 ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),\
                 ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
                 ('California', 'Sacramento', '38.555605', '-121.468926')]

    shifted_4 = [('California', 'Sacramento', '38.555605', '-121.468926'),\
                 ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),\
                 ('Georgia', 'Atlanta', '33.76', '-84.39'),\
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
                 ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),\
                 ('Colorado', 'Denver', '39.7391667', '-104.984167')]
    
    assert shift_cities(road_map4) ==\
    (shifted_4)

def test_shift_cities_5():
    """
    Testing that the function still runs if only given one city
    """
    road_map5 = [('Hawaii', 'Honolulu', '21.30895', '-157.826182')]
    
    shifted_5 = [('Hawaii', 'Honolulu', '21.30895', '-157.826182')]
    
    assert shift_cities(road_map5) ==\
    (shifted_5)
