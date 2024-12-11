import getOrderItemsResponse from "../../res/getOrderItemsResponse.json" with { type: 'json' };
import express from "express";

const router = express.Router();
router.get('/orders/:orderId/orderItems', (req, res)=>{
    res.json(getOrderItemsResponse)
});

export default router;