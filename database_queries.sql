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
VALUES ('CA', '90001', 'Oxnard Dr', 4556418275026205, (SELECT c_id FROM public."Customer" WHERE c_username='jjohnson'),'Los Angeles'),
('IL', '60616', 'Michigan Ave', 5497021817479673, (SELECT c_id FROM public."Customer" WHERE c_username='esander'),'Chicago'),
('TN', '37830', 'Cumberland Dr', 4532271942188968, (SELECT c_id FROM public."Customer" WHERE c_username='svoski'),'Knoxville'),
('PA', '19092', 'Hamilton St', 4916238378558887, (SELECT c_id FROM public."Customer" WHERE c_username='pjameson'),'Philadelphia'),
('NM', '87532', 'Kristi Ln', 6011415012494351, (SELECT c_id FROM public."Customer" WHERE c_username='tyang'),'Los Alamos'),
('FL', '32003', 'Palm Dr', 4916203781250266, (SELECT c_id FROM public."Customer" WHERE c_username='mpereira'),'Miami');

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
insert into cost("product_id", "state", "price")
values (1, 'CA', 10),
(1, 'IL', 8),
(1, 'FL', 6),
(1, 'TN', 4),
(1, 'PA', 7),
(1, 'NM', 3),
(2, 'CA', 4),
(2, 'IL', 3),
(2, 'FL', 2),
(2, 'TN', 2),
(2, 'PA', 3),
(2, 'NM', 1),
(3, 'CA', 8),
(3, 'IL', 5),
(3, 'FL', 6),
(3, 'TN', 4),
(3, 'PA', 7),
(3, 'NM', 4),
(4, 'CA', 4),
(4, 'IL', 2),
(4, 'FL', 2),
(4, 'TN', 3),
(4, 'PA', 1),
(4, 'NM', 2),
(5, 'CA', 10),
(5, 'IL', 8),
(5, 'FL', 9),
(5, 'TN', 8),
(5, 'PA', 6),
(5, 'NM', 5),
(6, 'CA', 12),
(6, 'IL', 10),
(6, 'FL', 9),
(6, 'TN', 7),
(6, 'PA', 8),
(6, 'NM', 6),
(7, 'CA', 20),
(7, 'IL', 16),
(7, 'FL', 19),
(7, 'TN', 20),
(7, 'PA', 14),
(7, 'NM', 10);

/*stock table*/
insert into stock("warehouse_id", "quantity", "product_id")
values(1, 7100, 1),
(1, 6100, 2),
(1, 2100, 3),
(1, 3000, 4),
(1, 3200, 5),
(1, 8000, 6),
(1, 4300, 7),
(2, 3200, 1),
(2, 3400, 2),
(2, 1900, 3),
(2, 2300, 4),
(2, 5300, 5),
(2, 1200, 6),
(2, 4500, 7),
(3, 2100, 1),
(3, 1500, 2),
(3, 1200, 3),
(3, 6400, 4),
(3, 1600, 5),
(3, 1200, 6),
(3, 900, 7);

/*warehouse table*/ 
insert into warehouse("warehouse_id", "street", "zip", "state", "capacity", "city")
values (default, '2100 Rodeo Dr', 94002, 'CA', 80000, 'Los Angeles'),
(default, '400 Madison Ave', 60615, 'IL', 100000, 'Chicago'),
(default, '4210 S Walnut St', 15001, 'PA', 75000, 'Philadelphia');


/*staff table*/
insert into staff("first_name", "last_name", "job_title", "s_username", "password", "salary", "state", "street", "zip", "city")
values ('Stewart', 'Maggie', 'Manager', 'mstewart', 'stewartmanage1', 80000, 'CA', '127 Patrick Blvd', 94002, 'Los Angeles'),
('Pulliam', 'John', 'Worker', 'jpulliam', 'pulliamworker1', 50000, 'CA', '240 Miami St', 94002, 'Los Angeles'),
('Rodriguez', 'Calvin', 'Manager', 'crodriguez', 'rodriguezmanage2', 70000, 'IL', '100 Wabash Ave', 60616, 'Chicago'),
('Madison', 'Katie', 'Worker', 'kmadison', 'madisonworker2', 45000, 'IL', '2100 State St', 60616, 'Chicago'),
('Rajesh', 'Daniel', 'Manager', 'drajesh', 'rajeshmanage3', 75000, 'PA', '2240 S Walnut St', 19109, 'Philadelphia'),
('Jackson', 'Melissa', 'Worker', 'mjackson', 'jacksonworker3', 55000, 'PA', '150 Center Dr', 19109, 'Philadelphia');







