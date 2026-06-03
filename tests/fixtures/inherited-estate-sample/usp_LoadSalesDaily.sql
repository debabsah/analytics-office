CREATE PROCEDURE dbo.usp_LoadSalesDaily AS
BEGIN
    TRUNCATE TABLE dbo.SalesDaily;
    INSERT INTO dbo.SalesDaily (SaleDate, RegionID, NetAmount)
    SELECT s.SaleDate, s.RegionID, s.GrossAmount - s.ReturnsAmount
    FROM dbo.SalesStage s          -- NOTE: nothing in this estate populates SalesStage
    WHERE s.RegionID = 7;          -- NOTE: hardcoded region, unexplained
END
