import getOrderItemsResponse from "../../res/responses/getOrderItemsResponse.json" with { type: 'json' };
import express from "express";

const app = express();
app.get('/orders/:orderId/orderItems', (req, res)=>{
    res.json(getOrderItemsResponse)
});

app.patch('/orders/:orderId/regulatedInfo', (req, res)=>{
    res.status(204).send();
});

export default app;