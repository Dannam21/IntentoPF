const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { tenant_id, category_id, name, description } = JSON.parse(event.body);

    const params = {
        TableName: 'Categories',
        Item: {
            tenant_id,        // Clave de partición
            category_id,      // Clave de ordenamiento
            name,
            description
        }
    };

    try {
        await dynamoDB.put(params).promise();
        return { statusCode: 201, body: JSON.stringify({ message: 'Category created successfully!' }) };
    } catch (err) {
        return { statusCode: 500, body: JSON.stringify(err) };
    }
};
