package com.amazon.SellingPartnerAPI.api.commons;

import com.amazon.SellingPartnerAPIAA.LWAAuthorizationCredentials;

import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Objects;

public abstract class ApiTest {
   protected static String endpoint = "http://localhost:3000";
   protected static String authEndpoint = "http://localhost:3000/auth/o2/token";
   protected static LWAAuthorizationCredentials credentials = LWAAuthorizationCredentials.builder()
           .clientId("clientId")
           .clientSecret("clientSecret")
           .refreshToken("refreshToken")
           .endpoint(authEndpoint)
           .build();

   protected Reader getRequestFile(String fileName) {
      return new InputStreamReader(
              Objects.requireNonNull(this.getClass().getResourceAsStream("/res/requests/" + fileName))
      );
   }
}
