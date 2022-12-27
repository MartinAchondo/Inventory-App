
Private Sub workbook_open()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    Dim sh2 As Worksheet
    Set sh2 = ThisWorkbook.Sheets("Sheet2")
    sh2.Visible = xlSheetVeryHidden
    Dim valor As String
    valor = sh2.Range("A1").Value
    If valor = "sos" Then
        Call borrar_titulos
        Call agregar_titulos
        Call crear_tabla
        Call decorar_tabla
        sh2.Range("A1").Value = "No"
    End If
    ThisWorkbook.Save
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
End Sub


Private Sub borrar_titulos()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Ventas")
    
    Dim rng As Range
    Set rng = sh.Rows(1)
    rng.EntireRow.Delete
    
    Set rng = sh.Columns("A:A")
    rng.EntireColumn.Delete
    
    Set rng = sh.Rows(1)
    rng.EntireRow.Insert
End Sub

Private Sub agregar_titulos()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Ventas")
    Dim data As Variant
    
    data = Array("Id Venta", "Código", "Descripcion", "Color", "Fecha", "Cantidad", "Lugar", "Precio Real", "Precio Venta", "Descuento")
    
    For j = 0 To UBound(data)
        sh.Cells(1, j + 1).Value = data(j)
    Next j
    
End Sub

Private Sub crear_tabla()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Ventas")
    
    Dim lRow As Long
    lRow = sh.Cells(Rows.Count, 1).End(xlUp).Row
    Dim cell As String
    cell = "A1:J" & lRow

    sh.ListObjects.Add(xlSrcRange, Range("$A$1:$J$" & lRow), , xlYes).Name = _
        "Tabla1"
    sh.ListObjects("Tabla1").TableStyle = "TableStyleLight1"
     
End Sub

Sub decorar_tabla()

    Dim lRow As Long
    lRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Ventas")
    
    Dim rng As Range
    Set rng = sh.Columns("A:J")
    rng.ColumnWidth = 12.91
    
    Set rng = sh.Rows("1:" & lRow)
    rng.RowHeight = 20.5
    
    Set rng = sh.Range("Tabla1[#All]")
    
    With rng
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    With rng
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    
    Set rng = sh.Columns("H:H")
    rng.Style = "Currency [0]"
        Set rng = sh.Columns("I:I")
    rng.Style = "Currency [0]"
    
    Set rng = sh.Range("Tabla1[#Headers]")
    With rng.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent1
        .TintAndShade = 0.399975585192419
        .PatternTintAndShade = 0
    End With
    
    Set rng = sh.Range("Tabla1[#All]")
    rng.Borders(xlDiagonalDown).LineStyle = xlNone
    rng.Borders(xlDiagonalUp).LineStyle = xlNone
    With rng.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlMedium
    End With
    With rng.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlMedium
    End With
    With rng.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlMedium
    End With
    With rng.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlMedium
    End With
    rng.Borders(xlInsideVertical).LineStyle = xlNone
    rng.Borders(xlInsideHorizontal).LineStyle = xlNone

    Set rng = sh.Columns("C:C")
    With rng
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    rng.ColumnWidth = 37.91
    
    Set rng = sh.Range("C1")
    With rng
        .HorizontalAlignment = xlCenter
    End With
    
End Sub

