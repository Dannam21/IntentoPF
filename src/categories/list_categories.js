const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { tenant_id } = event.queryStringParameters;

    const params = {
        TableName: 'Categories',
        KeyConditionExpression: 'tenant_id = :tenant_id',
        ExpressionAttributeValues: {
            ':tenant_id': tenant_id
        }
    };

    try {
        const data = await dynamoDB.query(params).promise();
        return { statusCode: 200, body: JSON.stringify(data.Items) };
    } catch (err) {
        return { statusCode: 500, body: JSON.stringify(err) };
    }
};
