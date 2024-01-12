FROM golang:1.21.5-alpine as builder
WORKDIR /build
COPY go.mod . 
RUN go mod download
COPY . .
RUN go build -o /main backend.go

FROM alpine:3
COPY --from=builder main /bin/main
ENTRYPOINT ["/bin/main"]
