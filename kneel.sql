CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` VARCHAR(160) NOT NULL,
    `price` NUMERIC(6,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC (3,2) NOT NULL,
    `price` NUMERIC (6,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` VARCHAR(50) NOT NULL,
    `price` NUMERIC (6,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `styles_id` INTEGER NOT NULL,
    `sizes_id` INTEGER NOT NULL,
    `metals_id` INTEGER NOT NULL,
    FOREIGN KEY(`metals_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`sizes_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`styles_id`) REFERENCES `Styles`(`id`)
);

--Sizes Data
INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 783);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);
--Styles Data
INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);
--Orders Data

INSERT INTO `Orders` VALUES (null, 3, 1, 4);
INSERT INTO `Orders` VALUES (null, 1, 4, 1);
INSERT INTO `Orders` VALUES (null, 1, 3, 2);
INSERT INTO `Orders` VALUES (null, 1, 2, 3);
INSERT INTO `Orders` VALUES (null, 1, 2, 1);

--Metals data
INSERT INTO `Metals` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metals` VALUES (null, "14k Gold", 736.4);
INSERT INTO `Metals` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metals` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metals` VALUES (null, "Palladium", 1241);



SELECT
    o.sizes_id,
    o.styles_id,
    o.metals_id,
    m.metal,
    m.price
FROM `Orders` o
JOIN Metals m ON m.id = o.metals_id

SELECT
    o.id,
    o.styles_id,
    o.sizes_id,
    o.metals_id,
    m.metal as metal,
    m.price as metal_price,
    s.style as style,
    s.price as style_price,
    sz.carets as carets,
    sz.price as size_price
FROM `Orders` o
JOIN Metals m ON m.id = o.metals_id
JOIN Styles s ON s.id = o.styles_id
JOIN Sizes sz ON sz.id = o.sizes_id





