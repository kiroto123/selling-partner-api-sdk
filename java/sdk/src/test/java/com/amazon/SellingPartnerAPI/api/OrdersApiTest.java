package com.amazon.SellingPartnerAPI.api;

import com.amazon.SellingPartnerAPI.JSON;
import com.amazon.SellingPartnerAPI.api.commons.ApiTest;
import com.amazon.SellingPartnerAPI.models.orders.GetOrderItemsResponse;
import com.amazon.SellingPartnerAPI.models.orders.UpdateVerificationStatusRequest;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.io.Reader;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;

public class OrdersApiTest extends ApiTest {

    private static OrdersApi ordersApi;

    @BeforeAll
    public static void beforeAll() {
        ordersApi = new OrdersApi.Builder()
            .lwaAuthorizationCredentials(credentials)
            .endpoint(endpoint)
            .build();
    }

    @Test
    public void getOrderItems() throws Exception {
        GetOrderItemsResponse response = ordersApi.getOrderItems("TEST_CASE_200", null);

        assertNotNull(response.getPayload());
        assertNull(response.getErrors());
    }

    @Test
    public void updateVerificationStatus() throws Exception {
        Reader reader = getRequestFile("updateVerificationStatusRequest.json");
        UpdateVerificationStatusRequest body = new JSON().getGson().fromJson(reader, UpdateVerificationStatusRequest.class);

        ordersApi.updateVerificationStatus(body, "902-3159896-1390916");
    }
}
