FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY FakeGen.csproj .
RUN dotnet restore
COPY Program.cs .
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/runtime:8.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "FakeGen.dll"]
