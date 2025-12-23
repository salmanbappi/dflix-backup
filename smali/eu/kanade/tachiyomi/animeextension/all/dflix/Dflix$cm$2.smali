.class final Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix$cm$2;
.super Lkotlin/jvm/internal/Lambda;
.source "Dflix.kt"

# interfaces
.implements Lkotlin/jvm/functions/Function0;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;-><init>()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x18
    name = null
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lkotlin/jvm/internal/Lambda;",
        "Lkotlin/jvm/functions/Function0<",
        "Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;",
        ">;"
    }
.end annotation

.annotation runtime Lkotlin/Metadata;
    d1 = {
        "\u0000\u0008\n\u0000\n\u0002\u0018\u0002\n\u0000\u0010\u0000\u001a\u00020\u0001H\n\u00a2\u0006\u0002\u0008\u0002"
    }
    d2 = {
        "<anonymous>",
        "Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;",
        "invoke"
    }
    k = 0x3
    mv = {
        0x1,
        0x8,
        0x0
    }
    xi = 0x30
.end annotation


# instance fields
.field final synthetic this$0:Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;


# direct methods
.method constructor <init>(Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;)V
    .locals 0

    iput-object p1, p0, Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix$cm$2;->this$0:Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;

    const/4 p1, 0x0

    invoke-direct {p0, p1}, Lkotlin/jvm/internal/Lambda;-><init>(I)V

    return-void
.end method


# virtual methods
.method public final invoke()Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;
    .locals 2

    .line 43
    new-instance v0, Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;

    iget-object v1, p0, Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix$cm$2;->this$0:Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;

    invoke-virtual {v1}, Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix;->getClient()Lokhttp3/OkHttpClient;

    move-result-object v1

    invoke-direct {v0, v1}, Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;-><init>(Lokhttp3/OkHttpClient;)V

    return-object v0
.end method

.method public bridge synthetic invoke()Ljava/lang/Object;
    .locals 1

    .line 43
    invoke-virtual {p0}, Leu/kanade/tachiyomi/animeextension/all/dflix/Dflix$cm$2;->invoke()Leu/kanade/tachiyomi/animeextension/all/dflix/CookieManager;

    move-result-object v0

    return-object v0
.end method
