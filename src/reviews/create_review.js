const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { tenant_id, product_id, review_id, username, rating, comment } = JSON.parse(event.body);

    const params = {
        TableName: 'Reviews',
        Item: {
            tenant_id,        // Clave de partición
            product_id,       // Clave de ordenamiento
            review_id,        // Un identificador único para la reseña
            username,
            rating,
            comment,
            created_at: new Date().toISOString()
        }
    };

    try {
        await dynamoDB.put(params).promise();
        return { statusCode: 201, body: JSON.stringify({ message: 'Review created successfully!' }) };
    } catch (err) {
        return { statusCode: 500, body: JSON.stringify(err) };
    }
};
