// Nombres de tablas DynamoDB
const TABLES = {
    USERS: 'Users',
    PRODUCTS: 'Products',
    REVIEWS: 'Reviews',
    CATEGORIES: 'Categories',
    ORDERS: 'Orders',
};

// Constantes para respuestas comunes
const RESPONSE_MESSAGES = {
    SUCCESS: 'Operación realizada con éxito',
    ERROR: 'Ha ocurrido un error',
    NOT_FOUND: 'Elemento no encontrado',
};

module.exports = {
    TABLES,
    RESPONSE_MESSAGES
};
