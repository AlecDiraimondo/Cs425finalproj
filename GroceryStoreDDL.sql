CREATE TABLE "Customer"(
	"first_name" varchar (20) NOT NULL,
	"last_name" varchar (20) NOT NULL,
	"c_id" serial,
	"c_username" varchar(20),
	"password" varchar(20),
	"balance" numeric(8,2) check ("balance">=0),
	PRIMARY KEY ("c_id")
);

CREATE TABLE "Creditcard"(
	"state" varchar(15) NOT NULL,
	"zipcode" int not null,
	"street" varchar(40) NOT NULL,
	"city" varchar(20),
	"card_number" bigint primary key,
	"c_id" serial
);

CREATE TABLE "Product"(
	"product_name" varchar(20),
	"product_category" varchar(20),
	"product_id" serial primary key,
	"size" int check("size" > 0)
);

CREATE TABLE "Shopping_cart"(
	"c_id" serial,
	"product_id" serial,
	"quantity" int check ("quantity">=0)
);

CREATE TABLE "Order"(
	"order_id" serial,
	"subtotal" numeric(8,2),
	"card_number" bigint,
	"time_ordered" timestamp,
	"status" varchar(10),
	check(status in ('ordered', 'sent', 'received')),
	PRIMARY KEY("order_id")
);

CREATE TABLE "Warehouse"(
	"warehouse_id" serial,
	"street" varchar(30) NOT NULL,	
	"zipcode" int NOT NULL,
	"city" varchar(20),
	"state" varchar(20) NOT NULL,
	"capacity" int check(capacity>0),
	PRIMARY KEY("warehouse_id")
);

CREATE TABLE "Stock"(
	"warehouse_id" serial,
	"quantity" int NOT NULL,
	"product_id" serial,
	PRIMARY KEY("warehouse_id", "product_id")
);

CREATE TABLE "Shipping_address"(
	"address_id" serial,
	"order_id" serial,
	"state" varchar(20) NOT NULL,
	"street" varchar(40) NOT NULL,
	"city" varchar(20),
	"zipcode" int NOT NULL,
	PRIMARY KEY("address_id")
);

CREATE TABLE "Cost"(
	"product_id" serial,
	"state" varchar(20),
	"price" numeric(8,2) check(price >=0),
	PRIMARY KEY("product_id","state")
);

CREATE TABLE "Staff"(
	"s_id" serial,
	"first_name" varchar(20) NOT NULL,
	"last_name" varchar(20) NOT NULL,
	"job_title" varchar(20),
	"s_username" varchar(20),
	"password" varchar(20),
	"salary" numeric (8,2) check ("salary" > 0),
	"state" varchar(20) NOT NULL,
	"street" varchar(20) NOT NULL,
	"city" varchar(20),
	"zipcode" int NOT NULL,
	PRIMARY KEY("s_id")
);
CREATE TABLE "Food"(
	"food_category" varchar(20),
	"product_id" serial,
	"calories" int check(calories > 0),
	PRIMARY KEY("product_id")
);

CREATE TABLE "Alcohol"(
	"alcohol_category" varchar(20),
	"alcohol_content" numeric (3,1),
	"product_id" serial,
	PRIMARY KEY("product_id")
);

ALTER TABLE "Shipping_address" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("order_id");
ALTER TABLE "Creditcard" ADD FOREIGN KEY ("c_id") REFERENCES "Customer"("c_id"); 
ALTER TABLE "Shopping_cart" ADD FOREIGN KEY ("c_id") REFERENCES "Customer"("c_id");
ALTER TABLE "Order" ADD FOREIGN KEY ("card_number") REFERENCES "Creditcard"("card_number");
ALTER TABLE "Stock" ADD FOREIGN KEY ("warehouse_id") REFERENCES "Warehouse"("warehouse_id");
ALTER TABLE "Cost" ADD FOREIGN KEY ("product_id") REFERENCES "Product"("product_id");
ALTER TABLE "Food" ADD FOREIGN KEY ("product_id") REFERENCES "Product"("product_id");
ALTER TABLE "Alcohol" ADD FOREIGN KEY ("product_id") REFERENCES "Product"("product_id");