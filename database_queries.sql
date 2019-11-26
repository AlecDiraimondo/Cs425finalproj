/*customer table*/
INSERT INTO public."Customer" ("first_name", "last_name", "c_id", "c_username", "password", "balance")
VALUES ('Johnson', 'Jake', DEFAULT, 'jjohnson', 'johnson68', '250'),
('Sander', 'Emily', DEFAULT, 'esander', 'sander82', '0'),
('Voski', 'Susan', DEFAULT, 'svoski', 'voski90', '50'),
('Jameson', 'Patrick', DEFAULT, 'pjameson', 'jameson62', '100'),
('Yang', 'Tom', DEFAULT, 'tyang', 'yang75', '20'),
('Pereira', 'Maxi', DEFAULT, 'mpereira', 'pereira61', '0');

/*creditcard table*/
INSERT INTO public."CreditCard" ("state", "zipcode", "street", "cardnumber", "c_id", "city")
VALUES ('CA', '90001', 'Oxnard Dr', '4556418275026205', (SELECT c_id FROM public."Customer" WHERE c_username='jjohnson'),'Los Angeles'),
('IL', '60616', 'Michigan Ave', '5497021817479673', (SELECT c_id FROM public."Customer" WHERE c_username='esander'),'Chicago'),
('TN', '37830', 'Cumberland Dr', '4532271942188968', (SELECT c_id FROM public."Customer" WHERE c_username='svoski'),'Knoxville'),
('PA', '19092', 'Hamilton St', '4916238378558887', (SELECT c_id FROM public."Customer" WHERE c_username='pjameson'),'Philadelphia'),
('NM', '87532', 'Kristi Ln', '6011415012494351', (SELECT c_id FROM public."Customer" WHERE c_username='tyang'),'Los Alamos'),
('FL', '32003', 'Palm Dr', '4916203781250266', (SELECT c_id FROM public."Customer" WHERE c_username='mpereira'),'Miami');

/*product table*/
INSERT INTO public."Product" ("product_name", "product_category", "product_id", "size")
VALUES('apples', 'food', default, 1),
('bananas', 'food', default, 1),
('rice', 'food', default, 2),
('bread', 'food', default, 0.5),
('beer','alcohol',default, 1),
('wine', 'alcohol', default, 1),
('vodka', 'alcohol', default, 1);

/*food table*/
INSERT INTO public."Food" ("food_category", "product_id", "calories")
VALUES ('fruit', (SELECT product_id FROM public."Product" WHERE product_name='apples'), 72),
('fruit', (SELECT product_id FROM public."Product" WHERE product_name='bananas'), 120),
('grain', (SELECT product_id FROM public."Product" WHERE product_name='rice'), 500),
('grain', (SELECT product_id FROM public."Product" WHERE product_name='bread'), 600);

/*alcohol table*/
INSERT INTO public."Alcohol" ("alcohol_category", "alcohol_content", "product_id")
values ('beers', '5', (SELECT product_id FROM public."Product" WHERE product_name='beer')),
('wines', '15', (SELECT product_id FROM public."Product" WHERE product_name='wine')),
('liquor', '50', (SELECT product_id FROM public."Product" WHERE product_name='vodka'));

/*cost table*/
insert into public."Cost"("product_id", "state", "price")
values ((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'CA', 10),
((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'IL', 8),
((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'FL', 6),
((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'TN', 4),
((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'PA', 7),
((SELECT product_id FROM public."Product" WHERE product_name='apples'), 'NM', 3),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'CA', 4),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'IL', 3),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'FL', 2),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'TN', 2),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'PA', 3),
((SELECT product_id FROM public."Product" WHERE product_name='bananas'), 'NM', 1),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'CA', 8),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'IL', 5),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'FL', 6),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'TN', 4),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'PA', 7),
((SELECT product_id FROM public."Product" WHERE product_name='rice'), 'NM', 4),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'CA', 4),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'IL', 2),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'FL', 2),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'TN', 3),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'PA', 1),
((SELECT product_id FROM public."Product" WHERE product_name='bread'), 'NM', 2),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'CA', 10),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'IL', 8),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'FL', 9),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'TN', 8),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'PA', 6),
((SELECT product_id FROM public."Product" WHERE product_name='beer'), 'NM', 5),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'CA', 12),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'IL', 10),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'FL', 9),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'TN', 7),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'PA', 8),
((SELECT product_id FROM public."Product" WHERE product_name='wine'), 'NM', 6),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'CA', 20),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'IL', 16),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'FL', 19),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'TN', 20),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'PA', 14),
((SELECT product_id FROM public."Product" WHERE product_name='vodka'), 'NM', 10);


/*stock table*/
insert into public."Stock"("warehouse_id", "quantity", "product_id")
values
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 7100, (SELECT product_id FROM public."Product" WHERE product_name='apples')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 6100, (SELECT product_id FROM public."Product" WHERE product_name='bananas')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 2100, (SELECT product_id FROM public."Product" WHERE product_name='rice')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 3000, (SELECT product_id FROM public."Product" WHERE product_name='bread')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 3200, (SELECT product_id FROM public."Product" WHERE product_name='beer')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 8000, (SELECT product_id FROM public."Product" WHERE product_name='wine')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=94002), 4300, (SELECT product_id FROM public."Product" WHERE product_name='vodka')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 3200, (SELECT product_id FROM public."Product" WHERE product_name='apples')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 3400, (SELECT product_id FROM public."Product" WHERE product_name='bananas')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 1900, (SELECT product_id FROM public."Product" WHERE product_name='rice')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 2300, (SELECT product_id FROM public."Product" WHERE product_name='bread')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 5300, (SELECT product_id FROM public."Product" WHERE product_name='beer')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 1200, (SELECT product_id FROM public."Product" WHERE product_name='wine')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=60615), 4500, (SELECT product_id FROM public."Product" WHERE product_name='vodka')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 2100, (SELECT product_id FROM public."Product" WHERE product_name='apples')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 1500, (SELECT product_id FROM public."Product" WHERE product_name='bananas')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 1200, (SELECT product_id FROM public."Product" WHERE product_name='rice')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 6400, (SELECT product_id FROM public."Product" WHERE product_name='bread')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 1600, (SELECT product_id FROM public."Product" WHERE product_name='beer')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 1200, (SELECT product_id FROM public."Product" WHERE product_name='wine')),
((SELECT warehouse_id FROM public."Warehouse" WHERE zipcode=15001), 900,  (SELECT product_id FROM public."Product" WHERE product_name='vodka'));

/*warehouse table*/ 
insert into public."Warehouse"("warehouse_id", "street", "zipcode", "state", "capacity", "city")
values (default, '2100 Rodeo Dr', 94002, 'CA', 80000, 'Los Angeles'),
(default, '400 Madison Ave', 60615, 'IL', 100000, 'Chicago'),
(default, '4210 S Walnut St', 15001, 'PA', 75000, 'Philadelphia');


/*staff table*/
insert into public."Staff"("first_name", "last_name", "job_title", "s_username", "password", "salary", "state", "street", "zip", "city")
values ('Stewart', 'Maggie', 'Manager', 'mstewart', 'stewartmanage1', 80000, 'CA', '127 Patrick Blvd', 94002, 'Los Angeles'),
('Pulliam', 'John', 'Worker', 'jpulliam', 'pulliamworker1', 50000, 'CA', '240 Miami St', 94002, 'Los Angeles'),
('Rodriguez', 'Calvin', 'Manager', 'crodriguez', 'rodriguezmanage2', 70000, 'IL', '100 Wabash Ave', 60616, 'Chicago'),
('Madison', 'Katie', 'Worker', 'kmadison', 'madisonworker2', 45000, 'IL', '2100 State St', 60616, 'Chicago'),
('Rajesh', 'Daniel', 'Manager', 'drajesh', 'rajeshmanage3', 75000, 'PA', '2240 S Walnut St', 19109, 'Philadelphia'),
('Jackson', 'Melissa', 'Worker', 'mjackson', 'jacksonworker3', 55000, 'PA', '150 Center Dr', 19109, 'Philadelphia');







