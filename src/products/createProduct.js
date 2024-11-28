const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { tenant_id, product_id, name, price, category } = JSON.parse(event.body);

    const params = {
        TableName: 'Products',
        Item: {
            tenant_id,
            product_id,
            name,
            price,
            category
        }
    };

    try {
        await dynamoDB.put(params).promise();
        return { statusCode: 201, body: JSON.stringify({ message: 'Product created successfully!' }) };
    } catch (err) {
        return { statusCode: 500, body: JSON.stringify(err) };
    }
};
