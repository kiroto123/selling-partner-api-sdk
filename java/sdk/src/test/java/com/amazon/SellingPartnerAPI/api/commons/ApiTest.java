package com.amazon.SellingPartnerAPI.api.commons;

import com.amazon.SellingPartnerAPIAA.LWAAuthorizationCredentials;

public abstract class ApiTest {
   protected static String endpoint = "http://localhost:3000";
   protected static String authEndpoint = "http://localhost:3000/auth/o2/token";
   protected static LWAAuthorizationCredentials credentials = LWAAuthorizationCredentials.builder()
           .clientId("clientId")
           .clientSecret("clientSecret")
           .refreshToken("refreshToken")
           .endpoint(authEndpoint)
           .build();
}
