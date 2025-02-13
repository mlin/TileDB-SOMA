is_arrow_object <- function(x) {
  inherits(x, "ArrowObject")
}

is_arrow_data_type <- function(x) {
  is_arrow_object(x) && inherits(x, "DataType")
}

is_arrow_record_batch <- function(x) {
  is_arrow_object(x) && inherits(x, "RecordBatch")
}

is_arrow_table <- function(x) {
  is_arrow_object(x) && inherits(x, "Table")
}

is_arrow_schema <- function(x) {
  is_arrow_object(x) && inherits(x, "Schema")
}

#' Convert Arrow types to supported TileDB type
#' List of TileDB types supported in R: https://github.com/TileDB-Inc/TileDB-R/blob/8014da156b5fee5b4cc221d57b4aa7d388abc968/inst/tinytest/test_dim.R#L97-L121
#'
#' List of all arrow types: https://github.com/apache/arrow/blob/90aac16761b7dbf5fe931bc8837cad5116939270/r/R/type.R#L700
#' @noRd

tiledb_type_from_arrow_type <- function(x) {
  stopifnot(is_arrow_data_type(x))
  switch(x$name,

    int8 = "INT8",
    int16 = "INT16",
    int32 = "INT32",
    int64 = "INT64",
    uint8 = "UINT8",
    uint16 = "UINT16",
    uint32 = "UINT32",
    uint64 = "UINT64",
    float32 = "FLOAT32",
    float = "FLOAT32",
    float64 = "FLOAT64",
    # based on tiledb::r_to_tiledb_type()
    double = "FLOAT64",
    boolean = "BOOL",
    bool = "BOOL",
    # large_utf8 = "large_string",
    # large_string = "large_string",
    # binary = "binary",
    # large_binary = "large_binary",
    # fixed_size_binary = "fixed_size_binary",
    # tiledb::r_to_tiledb_type() returns UTF8 for characters but they are
    # not yet queryable so we use ASCII for now
    utf8 = "ASCII",
    string = "ASCII",
    # date32 = "date32",
    # date64 = "date64",
    # time32 = "time32",
    # time64 = "time64",
    # null = "null",
    # timestamp = "timestamp",
    # decimal128 = "decimal128",
    # decimal256 = "decimal256",
    # struct = "struct",
    # list_of = "list",
    # list = "list",
    # large_list_of = "large_list",
    # large_list = "large_list",
    # fixed_size_list_of = "fixed_size_list",
    # fixed_size_list = "fixed_size_list",
    # map_of = "map",
    # duration = "duration",
    stop("Unsupported data type", call. = FALSE)
  )
}

#' Retrieve limits for Arrow types
#' @importFrom bit64 lim.integer64
#' @noRd
arrow_type_range <- function(x) {
  stopifnot(is_arrow_data_type(x))

  switch(x$name,
    int8 = c(-128L, 127L),
    int16 = c(-32768L, 32767L),
    int32 = c(-2147483647L, 2147483647L),
    int64 = bit64::lim.integer64(),
    uint8 = c(0L, 255L),
    uint16 = c(0L, 65535L),
    uint32 = bit64::as.integer64(c(0, 4294967295)),
    # We can't specify the full range of uint64 in R so we use the max of int64
    uint64 = c(bit64::as.integer64(0), bit64::lim.integer64()[2]),
    float32 = c(-3.4028235e+38, 3.4028235e+38),
    float = c(-3.4028235e+38, 3.4028235e+38),
    float64 = c(-1.7976931348623157e+308, 1.7976931348623157e+308),
    double =  c(-1.7976931348623157e+308, 1.7976931348623157e+308),
    boolean = NULL,
    bool = NULL,
    utf8 = NULL,
    string = NULL,
    stop("Unsupported data type", call. = FALSE)
  )
}
