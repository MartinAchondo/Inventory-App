Private Sub workbook_open()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    Dim sh, sh2 As Worksheet
    Set sh2 = ThisWorkbook.Sheets("Sheet2")
    sh2.Visible = xlSheetVeryHidden
    Dim valor As String
    valor = sh2.Range("A1").Value
    If valor = "sos" Then
        Set sh = ThisWorkbook.Sheets("Códigos")
        Call agregar_titulos(sh)
        Call crear_tabla(sh)
        Call decorar_tabla(sh)
        Call buscar_fotos(sh, sh2)
        sh2.Range("A1").Value = "No"
    End If
    ThisWorkbook.Save
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
End Sub

Private Sub agregar_titulos(sh)

    sh.Range("A1").EntireRow.Delete
    sh.Range("A1").EntireColumn.Delete
    sh.Range("A1").EntireRow.Insert
    Dim data As Variant
    data = Array("Código", "Descripción", "Foto")
    For j = 0 To UBound(data)
        sh.Cells(1, j + 1).Value = data(j)
    Next j

End Sub


Private Sub crear_tabla(sh)
    
    Dim lRow As Long
    lRow = Cells(Rows.Count, 1).End(xlUp).row
    Dim cell As String
    cell = "A1:C" & lRow

    sh.ListObjects.Add(xlSrcRange, Range("$A$1:$C$" & lRow), , xlYes).Name = _
        "Tabla1"
    sh.ListObjects("Tabla1").TableStyle = ""
    
End Sub

Sub decorar_tabla(sh)

    Dim lRow As Long
    lRow = Cells(Rows.Count, 1).End(xlUp).row

    Dim rng As Range
    Set rng = sh.Columns("A:A")
    rng.ColumnWidth = 15
    Set rng = sh.Columns("B:B")
    rng.ColumnWidth = 26
    Set rng = sh.Columns("C:C")
    rng.ColumnWidth = 26
    
    Set rng = sh.Rows("1:" & lRow)
    rng.RowHeight = 140
    
    Set rng = sh.Rows(1)
    rng.RowHeight = 30
    
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
    
    Set rng = sh.Columns("B:B")
    With rng
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlCenter
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Set rng = sh.Range("B1")
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
    
    sh.Range("A1").EntireColumn.Insert
    
End Sub

Sub buscar_fotos(sh, sh2)

    Dim lRow As Long
    Dim path, path2, path_foto, strFileExists As String
    path = sh2.Range("A2").Value
    lRow = sh.Cells(Rows.Count, 2).End(xlUp).row
    For j = 2 To lRow
        path2 = sh.Cells(j, 2).Value
        path_foto = path & "\" & path2 & ".jpg"
        strFileExists = Dir(path_foto)
        If strFileExists = "" Then
            path_foto = path & "\none.jpg"
        End If
        Call pegar_foto(path_foto, j, 4, sh)
    Next j

End Sub


Sub pegar_foto(path, row, column, sh)

    With sh.Pictures.Insert(path)
        With .ShapeRange
            .LockAspectRatio = msoTrue
            .Width = 30
            .Height = 108
        End With
        .Left = ActiveSheet.Cells(row, column).Left
        .Top = ActiveSheet.Cells(row, column).Top
        .Placement = 1
        .PrintObject = True
    End With

End Sub





