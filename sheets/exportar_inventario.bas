
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
        Call crear_tabla_tipos
        sh2.Range("A1").Value = "No"
    End If
    ThisWorkbook.Save
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
End Sub

Private Sub borrar_titulos()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Inventario")
    
    Dim rng As Range
    Set rng = sh.Rows(1)
    rng.EntireRow.Delete
    
    Set rng = sh.Columns("A:A")
    rng.EntireColumn.Delete
    Set rng = sh.Columns("A:A")
    rng.EntireColumn.Delete
    
    Set rng = sh.Rows(1)
    rng.EntireRow.Insert
End Sub

Private Sub agregar_titulos()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Inventario")
    Dim data As Variant
    
    data = Array("Código", "Tipo", "Descripción", "Color", "Costo", "Precio", "Cantidad", "Precio Tienda", "Cant. Casa", "Cant. Tienda")
    
    For j = 0 To UBound(data)
        sh.Cells(1, j + 1).Value = data(j)
    Next j

    sh.Columns("G:G").Cut Range("K1")
    sh.Columns("G:G").Delete Shift:=xlToLeft

End Sub

Private Sub crear_tabla()
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Inventario")
    
    Dim lRow As Long
    lRow = Cells(Rows.Count, 1).End(xlUp).Row
    Dim cell As String
    cell = "A1:J" & lRow

    sh.ListObjects.Add(xlSrcRange, Range("$A$1:$J$" & lRow), , xlYes).Name = _
        "tabla_inventario"
    sh.ListObjects("tabla_inventario").TableStyle = "TableStyleLight1"
     
End Sub


Sub decorar_tabla()

    Dim lRow As Long
    lRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    Dim sh As Worksheet
    Set sh = ThisWorkbook.Sheets("Inventario")
    
    Dim rng As Range
    Set rng = sh.Columns("A:J")
    rng.ColumnWidth = 12.91
    
    Set rng = sh.Rows("1:" & lRow)
    rng.RowHeight = 20.5
    
    Set rng = sh.Range("tabla_inventario[#All]")
    
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
    
    Set rng = sh.Columns("E:E")
    rng.Style = "Currency [0]"
    Set rng = sh.Columns("F:F")
    rng.Style = "Currency [0]"
    Set rng = sh.Columns("G:G")
    rng.Style = "Currency [0]"
    
    Set rng = sh.Range("tabla_inventario[#Headers]")
    With rng.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent1
        .TintAndShade = 0.399975585192419
        .PatternTintAndShade = 0
    End With
    
    Set rng = sh.Range("tabla_inventario[#All]")
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


Sub crear_tabla_tipos()
    Dim tabla As String
    tabla_dinamica = "tabla_dinamica"
    Dim sht As Worksheet
    Set sht = ThisWorkbook.Sheets("TablaTipos")
    sht.Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "tabla_inventario", Version:=7).CreatePivotTable TableDestination:="TablaTipos!R3C1", _
        TableName:=tabla_dinamica, DefaultVersion:=7
    With ActiveSheet.PivotTables(tabla_dinamica)
        .ColumnGrand = True
        .HasAutoFormat = True
        .DisplayErrorString = False
        .DisplayNullString = True
        .EnableDrilldown = True
        .ErrorString = ""
        .MergeLabels = False
        .NullString = ""
        .PageFieldOrder = 2
        .PageFieldWrapCount = 0
        .PreserveFormatting = True
        .RowGrand = True
        .SaveData = True
        .PrintTitles = False
        .RepeatItemsOnEachPrintedPage = True
        .TotalsAnnotation = False
        .CompactRowIndent = 1
        .InGridDropZones = False
        .DisplayFieldCaptions = True
        .DisplayMemberPropertyTooltips = False
        .DisplayContextTooltips = True
        .ShowDrillIndicators = True
        .PrintDrillIndicators = False
        .AllowMultipleFilters = False
        .SortUsingCustomLists = True
        .FieldListSortAscending = False
        .ShowValuesRow = False
        .CalculatedMembersInFilters = False
        .RowAxisLayout xlCompactRow
    End With
    With ActiveSheet.PivotTables(tabla_dinamica).PivotCache
        .RefreshOnFileOpen = False
        .MissingItemsLimit = xlMissingItemsDefault
    End With
    ActiveSheet.PivotTables(tabla_dinamica).RepeatAllLabels xlRepeatLabels
    ActiveWorkbook.ShowPivotTableFieldList = True
    With ActiveSheet.PivotTables(tabla_dinamica).PivotFields("Tipo")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables(tabla_dinamica).PivotFields("Código")
        .Orientation = xlRowField
        .Position = 2
    End With
    With ActiveSheet.PivotTables(tabla_dinamica).PivotFields("Descripción")
        .Orientation = xlRowField
        .Position = 3
    End With
    
    ActiveSheet.PivotTables(tabla_dinamica).AddDataField ActiveSheet.PivotTables( _
        tabla_dinamica).PivotFields("Cantidad"), "Suma de Cantidad", xlSum
    ActiveWorkbook.ShowPivotTableFieldList = False
    ActiveSheet.PivotTables(tabla_dinamica).AddDataField ActiveSheet.PivotTables( _
        tabla_dinamica).PivotFields("Cant. Casa"), "Suma de Cant. Casa", xlSum
    ActiveSheet.PivotTables(tabla_dinamica).AddDataField ActiveSheet.PivotTables( _
        tabla_dinamica).PivotFields("Cant. Tienda"), "Suma de Cant. Tienda", xlSum
    
    ActiveSheet.PivotTables(tabla_dinamica).CompactLayoutRowHeader = "Inventario"
    ActiveSheet.PivotTables(tabla_dinamica).TableStyle2 = "PivotStyleMedium9"
    ActiveSheet.PivotTables(tabla_dinamica).ClearAllFilters
    ActiveSheet.PivotTables(tabla_dinamica).PivotFields("Tipo").ShowDetail = False
    
    ActiveSheet.Shapes.AddChart2(251, xlPie).Select
    ActiveChart.SetSourceData Source:=Range("TablaTipos!$A$3:$D$12")
    ActiveSheet.Shapes("Gráfico 1").IncrementLeft 157
    ActiveSheet.Shapes("Gráfico 1").IncrementTop -20
    ActiveSheet.Shapes("Gráfico 1").ScaleWidth 1.2145833333, msoFalse, _
        msoScaleFromTopLeft
    ActiveSheet.Shapes("Gráfico 1").ScaleHeight 1.1770833333, msoFalse, _
        msoScaleFromTopLeft
    ActiveChart.Legend.Select
    Selection.Top = 17.937
    Selection.Height = 185.464
    Selection.Left = 341.75
    Selection.Width = 89.5

    ThisWorkbook.Sheets("Inventario").Select

End Sub

Sub guardar_como()

    Dim folder As String
    With Application.FileDialog(4)
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub
        folder = .SelectedItems(1)
    End With
    Application.DisplayAlerts = False
    fecha = ThisWorkbook.Sheets("Sheet2").Range("A2").Value
    ActiveWorkbook.SaveCopyAs folder & "\Inventario" & fecha & ".xlsm"
    Application.DisplayAlerts = True
End Sub


