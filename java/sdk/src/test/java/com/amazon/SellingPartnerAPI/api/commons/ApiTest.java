package com.amazon.SellingPartnerAPI.api.commons;

import com.amazon.SellingPartnerAPIAA.LWAAuthorizationCredentials;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse.BodyHandlers;

public abstract class ApiTest {
   protected static String endpoint = "http://localhost:3000";
   protected static String authEndpoint = "http://localhost:3000/auth/o2/token";
   protected static LWAAuthorizationCredentials credentials = LWAAuthorizationCredentials.builder()
           .clientId("clientId")
           .clientSecret("clientSecret")
           .refreshToken("refreshToken")
           .endpoint(authEndpoint)
           .build();

   protected void instructBackendMock(String response, String code) throws Exception {
      HttpRequest request = HttpRequest.newBuilder()
              .uri(new URI(endpoint + "/response/" + response + "/code/" + code))
              .POST(HttpRequest.BodyPublishers.noBody())
              .build();

      HttpClient.newHttpClient().send(request, BodyHandlers.discarding());
   }
}